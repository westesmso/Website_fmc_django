# Entidades e Classes

Projeto: website_fmc_django  
App: fmc  
Gerado em: 2026-07-07

## Sumario

- [Resumo](#resumo)
- [Entidades](#entidades)
- [Classes da Aplicacao](#classes-da-aplicacao)
- [Relacoes](#relacoes)

## Resumo

- O sistema possui tres entidades de lead separadas por contexto de negocio: contato, trabalhe-conosco e cotacao.
- As entidades nao possuem relacionamento direto (ForeignKey), mas compartilham padrao estrutural comum.

## Entidades

### LeadContato

- Modulo: `fmc.models`
- Tabela: `fmc_leadcontato`
- Finalidade: Armazenar leads enviados pelo formulario de contato.

Campos:

- `nome`: CharField, max_length=200, obrigatorio
- `email`: EmailField, obrigatorio
- `mensagem`: TextField, obrigatorio
- `criado_em`: DateTimeField, auto_now_add, obrigatorio

Meta:

- ordering: `-criado_em`
- verbose_name: Lead de Contato

Metodo:

- `__str__() -> str`: Retorna representacao amigavel para admin e logs.

### LeadTrabalhe

- Modulo: `fmc.models`
- Tabela: `fmc_leadtrabalhe`
- Finalidade: Armazenar leads do formulario trabalhe conosco.

Campos:

- `nome`: CharField, max_length=200, obrigatorio
- `telefone`: CharField, max_length=30, obrigatorio
- `descricao`: TextField, obrigatorio
- `criado_em`: DateTimeField, auto_now_add, obrigatorio

Meta:

- ordering: `-criado_em`
- verbose_name: Lead Trabalhe Conosco

Metodo:

- `__str__() -> str`: Retorna representacao amigavel para admin e logs.

### LeadCotacao

- Modulo: `fmc.models`
- Tabela: `fmc_leadcotacao`
- Finalidade: Armazenar leads de solicitacao de cotacao para eventos.

Campos:

- `nome`: CharField, max_length=200, obrigatorio
- `email`: EmailField, obrigatorio
- `mensagem`: TextField, obrigatorio
- `criado_em`: DateTimeField, auto_now_add, obrigatorio

Meta:

- ordering: `-criado_em`
- verbose_name: Lead Cotacao de Evento

Metodo:

- `__str__() -> str`: Retorna representacao amigavel para admin e logs.

## Classes da Aplicacao

- `ContatoForm` (`fmc.forms`, `forms.Form`): valida input do formulario de contato.
- `TrabalheForm` (`fmc.forms`, `forms.Form`): valida input do formulario trabalhe conosco.
- `CotacaoForm` (`fmc.forms`, `forms.Form`): valida input do formulario de cotacao.
- `LeadContatoAdmin` (`fmc.admin`, `admin.ModelAdmin`): administracao de LeadContato no Django Admin.
- `LeadTrabalheAdmin` (`fmc.admin`, `admin.ModelAdmin`): administracao de LeadTrabalhe no Django Admin.
- `LeadCotacaoAdmin` (`fmc.admin`, `admin.ModelAdmin`): administracao de LeadCotacao no Django Admin.

## Relacoes

- Dependencia em camadas: `fmc.views` -> `fmc.forms` (validacao de entrada).
- Dependencia em camadas: `fmc.views` -> `fmc.models` (persistencia dos leads).
- Registro administrativo: `fmc.admin` -> `fmc.models` (registro no Django Admin).
- Injecao de contexto: `fmc.context_processors.site_config` -> templates (dados institucionais globais).
