from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True) #vai criar a chave primeira automaticamente
    nome = models.TextField(max_length=255) #campo de texto
    idade = models.IntegerField() #campo de numero inteiro
