"""
Base settings shared across environments.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def _load_dotenv(dotenv_path: Path) -> None:
    if not dotenv_path.exists():
        return

    for raw_line in dotenv_path.read_text(encoding='utf-8').splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue

        key, value = line.split('=', 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        if key and key not in os.environ:
            os.environ[key] = value


def _to_bool(value: str, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {'1', 'true', 'yes', 'on'}


def _to_int(value: str, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


_load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-change-me')
DEBUG = _to_bool(os.getenv('DJANGO_DEBUG', 'False'), default=False)

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
    if host.strip()
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fmc',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website_fmc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'fmc.context_processors.site_config',
            ],
        },
    },
]

WSGI_APPLICATION = 'website_fmc.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Cache settings (task 12)
FMC_PUBLIC_PAGE_CACHE_SECONDS = _to_int(os.getenv('FMC_PUBLIC_PAGE_CACHE_SECONDS', '300'), 300)

CACHES = {
    'default': {
        'BACKEND': os.getenv('DJANGO_CACHE_BACKEND', 'django.core.cache.backends.locmem.LocMemCache'),
        'LOCATION': os.getenv('DJANGO_CACHE_LOCATION', 'website-fmc-cache'),
        'TIMEOUT': FMC_PUBLIC_PAGE_CACHE_SECONDS,
    }
}

# Email settings (task 11)
EMAIL_BACKEND = os.getenv('DJANGO_EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
DEFAULT_FROM_EMAIL = os.getenv('DJANGO_DEFAULT_FROM_EMAIL', 'noreply@example.com')
EMAIL_HOST = os.getenv('DJANGO_EMAIL_HOST', 'localhost')
EMAIL_PORT = _to_int(os.getenv('DJANGO_EMAIL_PORT', '25'), 25)
EMAIL_HOST_USER = os.getenv('DJANGO_EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('DJANGO_EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = _to_bool(os.getenv('DJANGO_EMAIL_USE_TLS', 'False'), default=False)
EMAIL_USE_SSL = _to_bool(os.getenv('DJANGO_EMAIL_USE_SSL', 'False'), default=False)

FMC_EMAIL_NOTIFICATIONS_ENABLED = _to_bool(
    os.getenv('FMC_EMAIL_NOTIFICATIONS_ENABLED', 'False'),
    default=False,
)
FMC_LEADS_EMAIL = os.getenv('FMC_LEADS_EMAIL', '')

FMC_SITE = {
    'brand_name': os.getenv('FMC_BRAND_NAME', 'YOUR_BRAND_NAME'),
    'emergency_phone_display': os.getenv('FMC_PHONE_DISPLAY', '(00) 00000-0000'),
    'phone_digits': os.getenv('FMC_PHONE_DIGITS', '5500000000000'),
    'address': os.getenv('FMC_ADDRESS', 'YOUR_CITY/STATE'),
    'email': os.getenv('FMC_EMAIL', 'contato@example.com'),
    'facebook_url': os.getenv(
        'FMC_FACEBOOK_URL',
        'https://www.facebook.com/your-page',
    ),
    'whatsapp_url': os.getenv(
        'FMC_WHATSAPP_URL',
        'https://wa.me/5500000000000',
    ),
    'whatsapp_cta_url': os.getenv(
        'FMC_WHATSAPP_CTA_URL',
        'https://api.whatsapp.com/send/?phone=5500000000000&text=Ola+Empresa%21+Vim+pelo+site.&type=phone_number&app_absent=0',
    ),
    'whatsapp_quote_url': os.getenv(
        'FMC_WHATSAPP_QUOTE_URL',
        'https://api.whatsapp.com/send/?phone=5500000000000&text=Ola+Empresa%21+Gostaria+de+solicitar+um+Orcamento.&type=phone_number&app_absent=0',
    ),
    'instagram_url': os.getenv(
        'FMC_INSTAGRAM_URL',
        'https://www.instagram.com/your-profile',
    ),
    'copyright_year': os.getenv('FMC_COPYRIGHT_YEAR', '2026'),
    'designer': os.getenv('FMC_DESIGNER', 'YOUR_DESIGNER'),
    'cnpj': os.getenv('FMC_CNPJ', '00.000.000/0000-00'),
}
