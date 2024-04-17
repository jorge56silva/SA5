from django.contrib import admin
from django.urls import path
from app_cadastro import views

urlpatterns = [
    path('', views.home, name='home'),  # Rota para a URL raiz
    path('criar/', views.criar_usuario, name='criar_usuario'),
    path('listar/', views.listar_usuarios, name='listar_usuarios'),
    path('atualizar/<int:pk>/', views.atualiza_usuario, name='atualiza_usuario'),
    path('deletar/<int:pk>/', views.deletar_usuario, name='deletar_usuario'),
    path('pesquisar/', views.pesquisar_usuarios, name='pesquisar_usuarios'),
    path('salvar_usuario/', views.salvar_usuario, name='salvar_usuario'),
]
