# Website FMC (Django)

Projeto web em Django para o site da FMC.

## Estrutura principal

- `manage.py`: utilitário principal do Django.
- `website_fmc/`: configurações globais do projeto.
- `fmc/`: app principal com views, urls e templates.
- `static/`: arquivos estáticos (CSS, JS, imagens).
- `db.sqlite3`: banco SQLite local.

## Requisitos

- Python 3.10+
- pip

## Configuração do ambiente

No PowerShell (Windows):

```powershell
# 1) Entrar na pasta do projeto
cd C:\xampp\htdocs\westes\Python\Website_FMC\Website_fmc_django

# 2) Criar ambiente virtual (caso ainda não exista)
python -m venv myvenv

# 3) Ativar ambiente virtual
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\myvenv\Scripts\Activate.ps1

# 4) Instalar dependências mínimas
pip install django
```

Observação: caso você já tenha o ambiente `myvenv` criado, basta ativá-lo e seguir.

## Rodando o projeto

```powershell
# Com o venv ativo:
python manage.py migrate
python manage.py runserver
```

Acesse no navegador:

- <http://127.0.0.1:8000/>

## Comandos úteis

```powershell
# Criar superusuário
python manage.py createsuperuser

# Coletar estáticos (produção)
python manage.py collectstatic

# Executar testes
python manage.py test
```

## Deploy (HostGator) com foco em static

Use este fluxo quando publicar em producao:

1. Ajuste o arquivo `.env` de producao:

```env
DJANGO_SETTINGS_MODULE=website_fmc.settings_prod
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
DJANGO_STATIC_URL=/static/
DJANGO_STATIC_ROOT=staticfiles
DJANGO_SECURE_SSL_REDIRECT=True
```

2. Acesse o projeto no servidor e ative o ambiente virtual.
3. Instale dependencias e rode migracoes:

```bash
pip install -r requirements.txt
python manage.py migrate
```

4. Gere os arquivos estaticos compilados:

```bash
python manage.py collectstatic --noinput
```

5. Verifique a pasta gerada `staticfiles/` no diretorio do projeto.
6. Configure o servidor web para servir `/static/` apontando para essa pasta `staticfiles/`.

Exemplo de ideia (o caminho real depende da sua conta no HostGator):

- URL: `/static/`
- Diretorio fisico: `/home/SEU_USUARIO/SEU_PROJETO/staticfiles/`

Se usar Python App no cPanel/Passenger, o mapeamento de static normalmente e feito por regra de servidor (Apache/Nginx) fora do Django.

7. Reinicie a aplicacao Python no painel da hospedagem.

### Como saber se o static ficou certo

1. Abra o site e use F12 (Network).
2. Recarregue a pagina.
3. Confirme que arquivos como `/static/fmc/css/site.css` respondem com status 200.
4. Se aparecer 404 em static, o problema e no mapeamento `/static/` -> `staticfiles/` no servidor.

## Documentacao tecnica (Markdown)

Todos os documentos estao em `documents/`.

- `documents/entities-and-classes.md`: entidades, classes, campos, metodos e relacoes em camadas.
- `documents/methods-and-behavior.md`: metodos/funcoes principais e comportamento por fluxo.
- `documents/routes-architecture.md`: arquitetura de rotas, handlers e redirects legados.
- `documents/software-architecture.md`: visao arquitetural por camadas (MVT) e fluxo de execucao.
- `documents/security-measures.md`: medidas de seguranca aplicadas e recomendacoes futuras.
- `documents/relevant-files-overview.md`: explicacao breve dos arquivos relevantes e suas funcoes.
- `documents/files-overview.md`: inventario resumido de arquivos e funcoes principais.
- `documents/improvement-plan.md`: plano de aprimoramento para escala, resiliencia e evolucao.

## Rotas e templates

As páginas principais estão no app `fmc`:

- templates em `fmc/templates/fmc/`
- estilos em `static/fmc/css/site.css`

## Boas práticas para desenvolvimento

- Não versionar `myvenv/`.
- Não versionar `db.sqlite3` (use apenas para desenvolvimento local).
- Definir `DEBUG=False` e `ALLOWED_HOSTS` corretamente em produção.
- Manter segredos fora do código (variáveis de ambiente).

## Licença

Defina aqui a licença do projeto (ex.: MIT, Proprietária etc.).
