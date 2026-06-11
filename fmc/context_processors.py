from django.conf import settings


def site_config(request):
    return {
        'site': settings.FMC_SITE,
    }
