# Arquivos Relevantes

Projeto: website_fmc_django  
Gerado em: 2026-07-07

## Sumario

- [Visao geral de arquivos](#visao-geral-de-arquivos)

## Visao geral de arquivos

- `manage.py` (bootstrap)
  - Entrada principal para comandos Django (`migrate`, `runserver`, `test`, `collectstatic`).

- `website_fmc/settings.py` (configuration)
  - Configuracao base: apps, middleware, templates, banco, cache, email e static.

- `website_fmc/settings_dev.py` (configuration-profile)
  - Perfil de desenvolvimento com `DEBUG` habilitado.

- `website_fmc/settings_prod.py` (configuration-profile)
  - Perfil de producao com hardening de seguranca e static com manifest.

- `website_fmc/urls.py` (routing)
  - Roteador raiz do projeto e definicao do handler de erro 404.

- `website_fmc/asgi.py` (deployment)
  - Ponto de entrada ASGI para servidores assincronos.

- `website_fmc/wsgi.py` (deployment)
  - Ponto de entrada WSGI para servidores compativeis com WSGI.

- `fmc/models.py` (domain-data)
  - Modelos de persistencia para leads de contato, trabalhe e cotacao.

- `fmc/forms.py` (input-validation)
  - Formularios de validacao para captacao de dados dos usuarios.

- `fmc/views.py` (application-flow)
  - Fluxo das paginas, processamento de formularios, persistencia e notificacao.

- `fmc/urls.py` (routing)
  - Rotas de pagina e redirecionamentos legados da migracao Flet para Django.

- `fmc/context_processors.py` (template-context)
  - Injeta dados de configuracao institucional para os templates.

- `fmc/admin.py` (operations)
  - Configuracao de listagem, filtros e busca dos leads no admin.

- `fmc/tests.py` (quality)
  - Testes basicos de rotas, redirecionamentos e envio de formularios.

- `static/` (frontend-assets)
  - Arquivos estaticos do projeto (css, imagens e recursos de interface).

- `fmc/templates/fmc/` (templates)
  - Templates das paginas renderizadas no servidor.

- `.env` (runtime-configuration)
  - Variaveis de ambiente para execucao local e, com ajustes, para producao.
