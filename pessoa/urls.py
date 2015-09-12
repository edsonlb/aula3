from django.conf.urls import include, url, patterns

urlpatterns = patterns('pessoa.views',
    url(r'^$', 'index'),
    url(r'^inserir/$', 'inserir'), 
    url(r'^excluir/(?P<codigo>\d+)/$', 'excluir'),
    url(r'^editar/(?P<codigo>\d+)/$', 'inserir'),
    url(r'^pesquisa/', 'pesquisa'),
    #url(r'^form/inserir/$', 'inserirForm', name='inserirForm'),
)
