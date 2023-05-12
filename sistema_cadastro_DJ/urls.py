
from django.contrib import admin
from django.urls import path
from app_sistema_cadastro import views

urlpatterns = [
    #estrutura a ser criada
    #rota, view responsável, nome de referência

    path('', views.home,name='home'), #o nome que vai ai é o caminha da URL que vem dps do endereço principal EX: facebook.com/"alguma coisa"
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
