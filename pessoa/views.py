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
