# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect

def index(request):
    return render(request, 'index.html', {'msg': u'É isso aí pessoal!'})
