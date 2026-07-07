# Arquitetura de Rotas

Projeto: website_fmc_django  
Gerado em: 2026-07-07

## Sumario

- [Roteador Raiz (website_fmc.urls)](#roteador-raiz-website_fmcurls)
- [Roteador da Aplicacao (fmc.urls)](#roteador-da-aplicacao-fmcurls)
- [Notas de roteamento](#notas-de-roteamento)

## Roteador Raiz (website_fmc.urls)

Rotas:

- `admin/` -> `django.contrib.admin.site.urls` (admin)
- `` (raiz) -> `include(fmc.urls)` (aplicacao)

Tratamento de erro:

- 404 -> `fmc.views.pagina_404`

## Roteador da Aplicacao (fmc.urls)

### Rotas principais

- `` -> `home` (`fmc.views.home`) [GET]
- `sobre/` -> `sobre` (`fmc.views.sobre`) [GET]
- `servicos/` -> `servicos` (`fmc.views.servicos`) [GET]
- `contato/` -> `contato` (`fmc.views.contato`) [GET, POST]
- `trabalhe-conosco/` -> `trabalhe-conosco` (`fmc.views.trabalhe`) [GET, POST]
- `cotacao-evento/` -> `cotacao` (`fmc.views.cotacao`) [GET, POST]

### Redirecionamentos legados (301)

- `home/` -> `home`
- `services/` -> `servicos`
- `about/` -> `sobre`
- `contact/` -> `contato`
- `work/` -> `trabalhe-conosco`
- `form1/` -> `cotacao`

## Notas de roteamento

- As rotas legadas preservam compatibilidade com URLs antigas do sistema baseado em Flet.
- As views institucionais utilizam cache de pagina para reduzir latencia.
