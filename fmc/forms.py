from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(
        max_length=200,
        label='Nome completo',
        error_messages={'required': 'Informe seu nome.'},
    )
    email = forms.EmailField(
        label='Email',
        error_messages={
            'required': 'Informe seu email.',
            'invalid': 'Digite um email valido.',
        },
    )
    mensagem = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        label='Mensagem',
        error_messages={'required': 'Escreva sua mensagem.'},
    )


class TrabalheForm(forms.Form):
    nome = forms.CharField(
        max_length=200,
        label='Nome',
        error_messages={'required': 'Informe seu nome.'},
    )
    telefone = forms.CharField(
        max_length=30,
        label='Telefone (WhatsApp)',
        error_messages={'required': 'Informe seu telefone.'},
    )
    descricao = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        label='Fale um pouco de voce',
        error_messages={'required': 'Escreva um pouco sobre voce.'},
    )


class CotacaoForm(forms.Form):
    nome = forms.CharField(
        max_length=200,
        label='Nome',
        error_messages={'required': 'Informe seu nome.'},
    )
    email = forms.EmailField(
        label='Email',
        error_messages={
            'required': 'Informe seu email.',
            'invalid': 'Digite um email valido.',
        },
    )
    mensagem = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        label='Detalhes do evento',
        error_messages={'required': 'Descreva o evento.'},
    )
