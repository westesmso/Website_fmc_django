# Arquitetura de Software

Projeto: website_fmc_django  
Gerado em: 2026-07-07

## Sumario

- [Estilo arquitetural: camadas (MVT)](#estilo-arquitetural-camadas-mvt)
- [Fluxo de execucao](#fluxo-de-execucao)
- [Atributos de qualidade](#atributos-de-qualidade)

## Estilo arquitetural: camadas (MVT)

### Camada de apresentacao

- Templates Django em `fmc/templates/fmc`
- Arquivos estaticos em `static/fmc`

### Camada de aplicacao

- Funcoes de fluxo HTTP em `fmc.views`
- Roteamento em `website_fmc.urls` e `fmc.urls`
- Context processor em `fmc.context_processors`

### Camada de dominio e dados

- Modelos de leads em `fmc.models`
- Persistencia via ORM Django (SQLite no estado atual)

### Camada de configuracao

- Configuracoes base em `website_fmc.settings`
- Perfis em `website_fmc.settings_dev` e `website_fmc.settings_prod`
- Variaveis de ambiente em `.env`

## Fluxo de execucao

1. Cliente requisita URL.
2. Roteador global delega para `fmc.urls`.
3. View processa entrada (forms em POST quando aplicavel).
4. Quando valido, dados sao persistidos em modelos e notificados por email.
5. Template e renderizado com dados de contexto (incluindo `site_config`).

## Atributos de qualidade

- Manutenibilidade: separacao clara entre rotas, views, forms, modelos e templates.
- Compatibilidade: redirecionamentos 301 mantem URLs legadas funcionando.
- Performance: cache de pagina configurado para rotas institucionais.
- Operabilidade: Admin Django para consulta e auditoria de leads.
