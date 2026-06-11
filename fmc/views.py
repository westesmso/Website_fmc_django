from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContatoForm, CotacaoForm, TrabalheForm
from .models import LeadContato, LeadCotacao, LeadTrabalhe


def pagina_404(request, exception=None):
    return render(request, 'fmc/404.html', status=404)


def home(request):
    return render(request, 'fmc/home.html')


def sobre(request):
    return render(request, 'fmc/sobre.html')


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
            messages.success(request, 'Cotacao enviada! Retornaremos com os detalhes.')
            return redirect('cotacao')
    else:
        form = CotacaoForm()

    return render(request, 'fmc/form1.html', {'form': form})
