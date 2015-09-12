# coding: UTF-8
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from pessoa.models import Pessoa
from pessoa.forms import PessoaFormulario
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _ 
# API
from pessoa.api import PessoaApi
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
import rest_framework_filters as filtro
from rest_framework.permissions import IsAdminUser
# FIM API

# CLIENTE API
#from django.shortcuts import HttpResponse
import requests
from requests.auth import HTTPDigestAuth
# FIM CLIENTE API

# CLIENTE API DEFINIÇÕES
def consulta_api(request):
    r = requests.get('https://apiedson.herokuapp.com/api/pessoa/?nome__icontains=a&ordering=nome', 
        auth=HTTPDigestAuth('admin','admin'))
    #print r
    #print ' '
    #print r.json()

    pessoas = r.json()['results']

    #print pessoas

    for pessoa in pessoas:
        print pessoa['nome'] + ' = ' + str(pessoa['idade'])

    return HttpResponse('SELECT - OK')

def incluir_api(request):
    valores = {'nome':'Zezinho', 'idade':'22', 'ano':'1'}

    r = requests.post('https://apiedson.herokuapp.com/api/pessoa/', 
        valores, 
        auth=HTTPDigestAuth('admin','admin') )

    print r.json()

    return HttpResponse('INSERT - OK')

def alterar_api(request):
    valores = {
    'id': '1', 
    'nome':'Alterado Edson Lopes 1', 
    'idade':'99', 
    'ano':'2020'}

    r = requests.post('https://apiedson.herokuapp.com/api_manual/',
        valores,
        auth=HTTPDigestAuth('admin','admin'))

    print r

    return HttpResponse('UPDATE - OK')










# FIM CLIENTE API DEFINIÇÕES








class Filtro_Pessoa(filtro.FilterSet):
    nome = filtro.AllLookupsFilter(name='nome')
    class Meta:
        model = Pessoa
        fields = ['nome','ano']


class Api_Automatica(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaApi
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('nome')
    filter_class = Filtro_Pessoa
    #permission_classes = (IsAdminUser,)
    #paginate_by = 3

@api_view(['POST','GET'])
def api_manual(request):

    if request.method == 'POST':
        if request.POST.get('id',None):
            try:
                pessoa = Pessoa.objects.get(pk=request.POST['id'])
            except:
                return Response("{ msg: 'Coloque um codigo correto'}", 
                status=status.HTTP_400_BAD_REQUEST)
        else:
            pessoa = Pessoa()

        pessoaApi = PessoaApi(pessoa, data=request.data, partial=True)

        if pessoaApi.is_valid():
            pessoaApi.save()
            return Response(pessoaApi.data, 
                status=status.HTTP_200_OK)
        else:
            return Response(pessoaApi.errors, 
                status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        pessoas = Pessoa.objects.all()[:3]
        pessoaApi = PessoaApi(pessoas, many=True)
        return Response(pessoaApi.data)

def inserir(request, codigo=0):
    if request.method == 'POST':
        try:
            pessoa = Pessoa.objects.get(pk=request.POST.get('id'))
            pessoa.nome = request.POST.get('nome')
            pessoa.idade = request.POST.get('idade')
        except:
            pessoa = Pessoa(
                nome=request.POST.get('nome'), 
                idade=request.POST.get('idade'), 
                ano=2015)

        pessoa.save()
        return HttpResponseRedirect('/')
    else:
        try:
            pessoa = Pessoa.objects.get(pk=codigo)
        except:
            pessoa = Pessoa()

        return render(request,'index.html',
                {'msg':_(u'Altere o registro'),'pessoa':pessoa})

def excluir(request, codigo):
    pessoa = Pessoa.objects.get(pk=codigo)
    pessoa.delete()
    return HttpResponseRedirect('/')

def pesquisa(request):
    
    if request.method == 'GET':
        selecao = {}

        if request.GET.get('busca'):
            selecao['nome__icontains'] = request.GET.get('busca')

        selecao['idade__gt'] = 12

        #print selecao

        pessoas = Pessoa.objects.filter(**selecao).order_by('-nome')
        #print pessoas[0].nome
        
        pessoas2 = Pessoa.objects.raw('select id from pessoa_pessoa where nome like "Olivaldo%"')

        #print Pessoa.objects.filter(telefone__telefone__icontains='5').count()
    
    return render(request,'index.html',
        {'msg':'Resultado da Busca','pessoas':pessoas})







