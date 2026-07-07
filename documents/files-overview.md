# Inventario de Arquivos e Funcoes

Projeto: Website FMC Django  
Versao: 1.0  
Gerado em: 2026-07-07

## Sumario

- [Arquivos](#arquivos)

## Arquivos

### manage.py

- Relevancia: alta
- Finalidade: ponto de entrada de comandos administrativos do Django.
- Funcao principal:
  - `main`: seleciona modulo de configuracoes e executa comandos (`runserver`, `migrate`, `test`, `collectstatic`).

### website_fmc/settings.py

- Relevancia: alta
- Finalidade: configuracao base do sistema.
- Funcao relevante:
  - `_load_dotenv`: carrega variaveis do `.env` para o ambiente do processo.

### website_fmc/settings_dev.py

- Relevancia: alta
- Finalidade: perfil de desenvolvimento.

### website_fmc/settings_prod.py

- Relevancia: alta
- Finalidade: perfil de producao com hardening de seguranca e static manifest.

### website_fmc/urls.py

- Relevancia: alta
- Finalidade: roteador global e handler de erro 404.

### website_fmc/wsgi.py

- Relevancia: media
- Finalidade: entrada WSGI para servidores sincronos.

### website_fmc/asgi.py

- Relevancia: media
- Finalidade: entrada ASGI para servidores assincronos.

### fmc/models.py

- Relevancia: alta
- Finalidade: define entidades de lead persistidas no banco.
- Funcoes relevantes:
  - `LeadContato.__str__`: representacao amigavel para admin e logs.
  - `LeadTrabalhe.__str__`: representacao amigavel para admin e logs.
  - `LeadCotacao.__str__`: representacao amigavel para admin e logs.

### fmc/forms.py

- Relevancia: alta
- Finalidade: valida entrada de dados dos formularios web.

### fmc/views.py

- Relevancia: alta
- Finalidade: controla fluxo HTTP de paginas e submissao de formularios.
- Funcoes relevantes:
  - `pagina_404`: renderiza pagina customizada de nao encontrado.
  - `_notify_lead`: envia notificacao de email para novo lead.
  - `home`: renderiza pagina inicial.
  - `sobre`: renderiza pagina institucional sobre a empresa.
  - `servicos`: renderiza pagina de servicos.
  - `contato`: processa formulario de contato e cria `LeadContato`.
  - `trabalhe`: processa formulario trabalhe conosco e cria `LeadTrabalhe`.
  - `cotacao`: processa formulario de cotacao e cria `LeadCotacao`.

### fmc/urls.py

- Relevancia: alta
- Finalidade: roteamento da aplicacao e redirecionamentos legados do Flet.

### fmc/admin.py

- Relevancia: media
- Finalidade: configuracao de exibicao e pesquisa dos leads no Django Admin.

### fmc/context_processors.py

- Relevancia: media
- Finalidade: disponibiliza configuracoes do site para todos os templates.
- Funcao relevante:
  - `site_config`: injeta dicionario `site` no contexto de template.

### fmc/tests.py

- Relevancia: alta
- Finalidade: testes automatizados de rotas, redirecionamentos e submissao de formularios.
