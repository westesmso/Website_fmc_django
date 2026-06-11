from django.db import models


class LeadContato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Lead de Contato'
        verbose_name_plural = 'Leads de Contato'
        ordering = ['-criado_em']

    def __str__(self):
        return f'{self.nome} — {self.email}'


class LeadTrabalhe(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=30)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Lead Trabalhe Conosco'
        verbose_name_plural = 'Leads Trabalhe Conosco'
        ordering = ['-criado_em']

    def __str__(self):
        return f'{self.nome} — {self.telefone}'


class LeadCotacao(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Lead Cotação de Evento'
        verbose_name_plural = 'Leads Cotação de Evento'
        ordering = ['-criado_em']

    def __str__(self):
        return f'{self.nome} — {self.email}'
