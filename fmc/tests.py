from django.test import TestCase
from django.urls import reverse

from .models import LeadContato, LeadCotacao, LeadTrabalhe


class RouteTests(TestCase):
	"""Valida disponibilidade das rotas principais e redirects legados."""

	def test_main_routes_should_return_200(self):
		urls = [
			reverse('home'),
			reverse('sobre'),
			reverse('servicos'),
			reverse('contato'),
			reverse('trabalhe-conosco'),
			reverse('cotacao'),
		]
		for url in urls:
			response = self.client.get(url)
			self.assertEqual(response.status_code, 200)

	def test_legacy_routes_should_redirect(self):
		legacy_urls = ['/home/', '/services/', '/about/', '/contact/', '/work/', '/form1/']
		for url in legacy_urls:
			response = self.client.get(url)
			self.assertEqual(response.status_code, 301)


class FormSubmissionTests(TestCase):
	"""Valida fluxos de submissao dos formularios publicos."""

	def test_contato_valid_should_create_lead(self):
		payload = {
			'nome': 'Joao da Silva',
			'email': 'joao@email.com',
			'mensagem': 'Mensagem de teste contato',
		}
		response = self.client.post(reverse('contato'), payload)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(LeadContato.objects.count(), 1)

	def test_trabalhe_valid_should_create_lead(self):
		payload = {
			'nome': 'Maria Souza',
			'telefone': '11999999999',
			'descricao': 'Tenho experiencia em atendimento pre-hospitalar',
		}
		response = self.client.post(reverse('trabalhe-conosco'), payload)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(LeadTrabalhe.objects.count(), 1)

	def test_cotacao_valid_should_create_lead(self):
		payload = {
			'nome': 'Empresa XPTO',
			'email': 'eventos@xpto.com',
			'mensagem': 'Preciso de ambulancia para evento com 500 pessoas.',
		}
		response = self.client.post(reverse('cotacao'), payload)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(LeadCotacao.objects.count(), 1)

	def test_contato_invalid_should_not_create_lead(self):
		payload = {
			'nome': '',
			'email': 'email-invalido',
			'mensagem': '',
		}
		response = self.client.post(reverse('contato'), payload)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(LeadContato.objects.count(), 0)
