from django.conf.urls import include, url
from django.contrib import admin
# API
from rest_framework import routers
from pessoa import views

rota = routers.DefaultRouter()
rota.register(r'pessoa', views.Api_Automatica, 'Pessoa')
# FIM API

urlpatterns = [
    url(r'^$', 'core.views.index'),
    url(r'^caminho/link1/$', 'core.views.link1', name='link1'),
    url(r'^caminho/link2/$', 'core.views.link2', name='link2'),
    url(r'^pessoa/', include('pessoa.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^api/', include(rota.urls)),
    url(r'^api_manual/$', 'pessoa.views.api_manual'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^consulta/api/$', 'pessoa.views.consulta_api'),
    url(r'^incluir/api/$', 'pessoa.views.incluir_api'),
    url(r'^alterar/api/$', 'pessoa.views.alterar_api'),


   
]
