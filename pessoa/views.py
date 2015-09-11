# coding: UTF-8
from django.shortcuts import render, HttpResponseRedirect
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
from django.views.decorators.csrf import csrf_exempt
# FIM API

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


def salva_api(request):
    return render(request,'cliente.html')









# =======================================================
def index(request):
    pessoas = Pessoa.objects.all()
    msg = _(u"Isso é uma vergonha.")
    return render(request,'conteudo.html',{'msg':msg,'pessoas':pessoas})

def inserirForm(request):
    if request.method == 'POST':
        form = PessoaFormulario(request.POST)

        if form.is_valid():
            dados = form.cleaned_data
            print dados['nome']

            request.session['sessao_nome'] = dados['nome'].upper()

            messages.info(request, 'Pessoa inserida com sucesso!')
            messages.success(request, 'Mais um teste!')

            form.save()
            return HttpResponseRedirect('/')
        else:    
            return render(request,'index.html',{'form':form})
    else:
        return HttpResponseRedirect('/')







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







