from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    nome = 'Fernando'
    turno = 't'
    lista_clientes = [
        { 'nome': 'Cassandra', 'sexo': 'f'},
        { 'nome': 'Leonel', 'sexo': 'm' },
        { 'nome': 'Geléia', 'sexo': 't' }
    ]
    dados_template = {'clientes': lista_clientes, 'nome': nome, 'turno': turno }
    return render(request, 'index.html', dados_template)
    #return HttpResponse('Olá mundo!')