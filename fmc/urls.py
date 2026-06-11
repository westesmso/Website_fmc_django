from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # Rotas principais
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('servicos/', views.servicos, name='servicos'),
    path('contato/', views.contato, name='contato'),
    path('trabalhe-conosco/', views.trabalhe, name='trabalhe-conosco'),
    path('cotacao-evento/', views.cotacao, name='cotacao'),

    # Aliases legados do Flet (redirect 301 permanente)
    path('home/', RedirectView.as_view(pattern_name='home', permanent=True)),
    path('services/', RedirectView.as_view(pattern_name='servicos', permanent=True)),
    path('about/', RedirectView.as_view(pattern_name='sobre', permanent=True)),
    path('contact/', RedirectView.as_view(pattern_name='contato', permanent=True)),
    path('work/', RedirectView.as_view(pattern_name='trabalhe-conosco', permanent=True)),
    path('form1/', RedirectView.as_view(pattern_name='cotacao', permanent=True)),
]