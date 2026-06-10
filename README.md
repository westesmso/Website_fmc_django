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
