# Metodos e Comportamento

Projeto: website_fmc_django  
Gerado em: 2026-07-07

## Sumario

- [Modulo fmc.views](#modulo-fmcviews)
- [Modulo fmc.models](#modulo-fmcmodels)
- [Modulo fmc.context_processors](#modulo-fmccontext_processors)

## Modulo fmc.views

- `pagina_404(request, exception) -> HttpResponse`
  - Renderiza pagina de erro customizada com status HTTP 404.

- `_notify_lead(subject: str, body: str) -> None`
  - Envia notificacao de novo lead para destinatario configurado no ambiente.
  - Observacao: usa `fail_silently=True` para nao interromper o fluxo de envio do formulario.

- `home(request) -> HttpResponse`
  - Renderiza pagina inicial institucional.
  - Cache: habilitado.

- `sobre(request) -> HttpResponse`
  - Renderiza pagina sobre a empresa.
  - Cache: habilitado.

- `servicos(request) -> HttpResponse`
  - Renderiza pagina de servicos.
  - Cache: habilitado.

- `contato(request) -> HttpResponse | HttpResponseRedirect`
  - Processa GET/POST do formulario de contato com validacao, persistencia e feedback ao usuario.
  - Fluxo: POST valido cria `LeadContato`, envia notificacao e redireciona.
  - Fluxo: POST invalido retorna pagina com erros do formulario.

- `trabalhe(request) -> HttpResponse | HttpResponseRedirect`
  - Processa formulario trabalhe conosco com validacao e persistencia em `LeadTrabalhe`.

- `cotacao(request) -> HttpResponse | HttpResponseRedirect`
  - Processa solicitacao de cotacao com validacao e persistencia em `LeadCotacao`.

## Modulo fmc.models

- `LeadContato.__str__() -> str`
  - Representacao textual amigavel para interface administrativa.

- `LeadTrabalhe.__str__() -> str`
  - Representacao textual amigavel para interface administrativa.

- `LeadCotacao.__str__() -> str`
  - Representacao textual amigavel para interface administrativa.

## Modulo fmc.context_processors

- `site_config(request) -> dict`
  - Entrega configuracoes de marca e contato para todos os templates.
