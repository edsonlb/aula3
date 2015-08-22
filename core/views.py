# coding: utf-8
from django.shortcuts import render
from pessoa.models import Pessoa
from pessoa.forms import PessoaFormulario

def index(request):
    pessoas = Pessoa.objects.all().order_by('nome')

    form = PessoaFormulario()

    return render(request, 'index.html', 
        {'msg': u'É isso aí pessoal!', 
        'pessoas':pessoas, 
        'form':form})

def link1(request):
    return render(request,'link1.html')

def link2(request):
    return render(request,'link2.html')
