from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_page

from .forms import ContatoForm, CotacaoForm, TrabalheForm
from .models import LeadContato, LeadCotacao, LeadTrabalhe


def pagina_404(request, exception=None):
    return render(request, 'fmc/404.html', status=404)


def _notify_lead(subject: str, body: str) -> None:
    send_mail(
        subject=subject,
        message=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.FMC_NOTIFY_EMAIL],
        fail_silently=True,
    )


@cache_page(settings.FMC_PAGE_CACHE_TIMEOUT)
def home(request):
    return render(request, 'fmc/home.html')


@cache_page(settings.FMC_PAGE_CACHE_TIMEOUT)
def sobre(request):
    return render(request, 'fmc/sobre.html')


@cache_page(settings.FMC_PAGE_CACHE_TIMEOUT)
def servicos(request):
    return render(request, 'fmc/servicos.html')


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            LeadContato.objects.create(
                nome=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                mensagem=form.cleaned_data['mensagem'],
            )
            _notify_lead(
                subject='Novo lead: Contato',
                body=(
                    f"Nome: {form.cleaned_data['nome']}\n"
                    f"Email: {form.cleaned_data['email']}\n\n"
                    f"Mensagem:\n{form.cleaned_data['mensagem']}"
                ),
            )
            messages.success(request, 'Mensagem enviada! Entraremos em contato em breve.')
            return redirect('contato')
    else:
        form = ContatoForm()

    return render(request, 'fmc/contato.html', {'form': form})


def trabalhe(request):
    if request.method == 'POST':
        form = TrabalheForm(request.POST)
        if form.is_valid():
            LeadTrabalhe.objects.create(
                nome=form.cleaned_data['nome'],
                telefone=form.cleaned_data['telefone'],
                descricao=form.cleaned_data['descricao'],
            )
            _notify_lead(
                subject='Novo lead: Trabalhe Conosco',
                body=(
                    f"Nome: {form.cleaned_data['nome']}\n"
                    f"Telefone: {form.cleaned_data['telefone']}\n\n"
                    f"Descricao:\n{form.cleaned_data['descricao']}"
                ),
            )
            messages.success(request, 'Cadastro recebido! Entraremos em contato.')
            return redirect('trabalhe-conosco')
    else:
        form = TrabalheForm()

    return render(request, 'fmc/trabalhe.html', {'form': form})


def cotacao(request):
    if request.method == 'POST':
        form = CotacaoForm(request.POST)
        if form.is_valid():
            LeadCotacao.objects.create(
                nome=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                mensagem=form.cleaned_data['mensagem'],
            )
            _notify_lead(
                subject='Novo lead: Cotacao de Evento',
                body=(
                    f"Nome: {form.cleaned_data['nome']}\n"
                    f"Email: {form.cleaned_data['email']}\n\n"
                    f"Detalhes:\n{form.cleaned_data['mensagem']}"
                ),
            )
            messages.success(request, 'Cotacao enviada! Retornaremos com os detalhes.')
            return redirect('cotacao')
    else:
        form = CotacaoForm()

    return render(request, 'fmc/form1.html', {'form': form})
