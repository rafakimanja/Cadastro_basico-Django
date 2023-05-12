from django.shortcuts import render
from .models import Usuario


def home(request): #request -> parâmetro que permite aceesar os dados que ja estão naquela pagina
    return render(request, 'usuarios/home.html') #render -> cria uma pagina (estão os dados do render)

def usuarios(request):
    novo_usuario = Usuario()
    
        #comando para pegar as infos dadas pelo usuario e colocar no banco de dados

        #um jeito de fazer 
    ''' nome = request.POST.get('nome') 
        idade = request.POST.get('idade')

        novo_usuario.nome = nome
        novo_usuario.idade = idade'''

    novo_usuario.nome = request.POST.get('nome') # (usa o nome dado lá no HTML, input name="..."')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #exibir todos os usuários já cadastrados em uma nova página (necessário usar o formato de dicionário)

    usuarios = {
        'usuarios': Usuario.objects.all() #retornando todos os dados direto do banco de dados 
    }

    #retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)