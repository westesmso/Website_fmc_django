# Plano de Melhorias

Projeto: website_fmc_django  
Gerado em: 2026-07-07

## Sumario

- [Objetivos](#objetivos)
- [Curto prazo (0-30 dias)](#curto-prazo-0-30-dias)
- [Medio prazo (1-3 meses)](#medio-prazo-1-3-meses)
- [Longo prazo (3-12 meses)](#longo-prazo-3-12-meses)

## Objetivos

- G-001: Escalabilidade de acesso e confiabilidade operacional.
- G-002: Aprimoramento de observabilidade e seguranca.
- G-003: Evolucao funcional do funil de leads.

## Curto prazo (0-30 dias)

- Prioridade alta: migrar banco de SQLite para PostgreSQL em producao.
  - Impacto esperado: melhora concorrencia, integridade transacional e recuperacao.

- Prioridade alta: adicionar logs estruturados para fluxo de formularios.
  - Impacto esperado: facilita suporte, auditoria e diagnostico de falhas.

- Prioridade media: adicionar testes para cenarios de erro de email.
  - Impacto esperado: garante estabilidade do fluxo mesmo com indisponibilidade SMTP.

## Medio prazo (1-3 meses)

- Prioridade alta: introduzir fila assincrona para notificacoes (Celery/RQ).
  - Impacto esperado: menor latencia no request web e maior resiliencia de entrega.

- Prioridade media: trocar cache local por Redis.
  - Impacto esperado: cache compartilhado entre multiplos processos/instancias.

- Prioridade media: implementar rate limiting e captcha opcional em formularios.
  - Impacto esperado: reduz spam e abuso automatizado.

## Longo prazo (3-12 meses)

- Prioridade alta: expor API para integracao com CRM.
  - Impacto esperado: automatiza distribuicao e rastreamento de leads.

- Prioridade media: instrumentar monitoramento APM e alertas.
  - Impacto esperado: deteccao proativa de degradacao e incidentes.

- Prioridade media: pipeline CI/CD com quality gates.
  - Impacto esperado: entrega mais segura, com testes e verificacoes automaticas.
