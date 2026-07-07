# Medidas de Seguranca

Projeto: website_fmc_django  
Gerado em: 2026-07-07

## Sumario

- [Medidas implementadas](#medidas-implementadas)
- [Recomendacoes futuras](#recomendacoes-futuras)

## Medidas implementadas

- SEC-001 (secrets-management) - implementado
  - Chaves e configuracoes sensiveis saem do codigo e vao para variaveis de ambiente.
  - Evidencia: `DJANGO_SECRET_KEY`, `EMAIL_HOST_PASSWORD` e demais variaveis no `.env`.

- SEC-002 (transport-and-cookies) - implementado no perfil de producao
  - Cookies de sessao e CSRF marcados como seguros no perfil de producao.
  - Evidencia: `SESSION_COOKIE_SECURE=True` e `CSRF_COOKIE_SECURE=True` em `settings_prod`.

- SEC-003 (http-hardening) - implementado no perfil de producao
  - Cabecalhos de seguranca e protecoes basicas ativas no perfil de producao.
  - Evidencia: `X_FRAME_OPTIONS=DENY`, `SECURE_CONTENT_TYPE_NOSNIFF=True`.

- SEC-004 (csrf) - implementado
  - Middleware CSRF ativo no stack padrao do Django.
  - Evidencia: `CsrfViewMiddleware` presente na configuracao de middleware.

- SEC-005 (host-header) - implementado
  - Restricao de hosts configuravel por `DJANGO_ALLOWED_HOSTS`.
  - Evidencia: `ALLOWED_HOSTS` carregado por variavel de ambiente.

- SEC-006 (input-validation) - implementado
  - Validacao de entrada realizada por forms Django em endpoints POST.
  - Evidencia: `ContatoForm`, `TrabalheForm` e `CotacaoForm`.

- SEC-007 (static-integrity) - implementado no perfil de producao
  - `ManifestStaticFilesStorage` ativo para versionamento e integridade de assets estaticos.
  - Evidencia: `STATICFILES_STORAGE` em `settings_prod`.

## Recomendacoes futuras

- SEC-NEXT-001 (alta): substituir SQLite por PostgreSQL em producao para robustez e concorrencia.
- SEC-NEXT-002 (alta): configurar backup automatico de banco e estrategia de restauracao testada.
- SEC-NEXT-003 (media): adicionar limite de taxa (rate limiting) para formularios publicos.
- SEC-NEXT-004 (media): adicionar CSP (Content Security Policy) adequada aos assets utilizados.
- SEC-NEXT-005 (media): usar backend de email transacional dedicado com monitoramento de entrega.
