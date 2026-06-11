from django.contrib import admin
from .models import LeadContato, LeadTrabalhe, LeadCotacao


@admin.register(LeadContato)
class LeadContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'criado_em')
    list_filter = ('criado_em',)
    search_fields = ('nome', 'email')
    readonly_fields = ('criado_em',)
    ordering = ('-criado_em',)


@admin.register(LeadTrabalhe)
class LeadTrabalheAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'criado_em')
    list_filter = ('criado_em',)
    search_fields = ('nome', 'telefone')
    readonly_fields = ('criado_em',)
    ordering = ('-criado_em',)


@admin.register(LeadCotacao)
class LeadCotacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'criado_em')
    list_filter = ('criado_em',)
    search_fields = ('nome', 'email')
    readonly_fields = ('criado_em',)
    ordering = ('-criado_em',)
