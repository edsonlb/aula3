# coding: UTF-8
from django.shortcuts import render, HttpResponseRedirect
from pessoa.models import Pessoa

def inserir(request):
    
    if request.method == 'POST':
        pessoa = Pessoa(
            nome=request.POST.get('nome'), 
            idade=request.POST.get('idade'), 
            ano=2015)

        pessoa.save()
    
    return HttpResponseRedirect('/')

def excluir(request, codigo):
    pessoa = Pessoa.objects.get(pk=codigo)
    pessoa.delete()
    return HttpResponseRedirect('/')

def pesquisa(request):
    
    if request.method == 'GET':
        pessoas = Pessoa.objects.filter(nome__contains=request.GET.get('busca'))
    
    return render(request,'index.html',
        {'msg':'Resultado da Busca','pessoas':pessoas})
