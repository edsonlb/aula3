from rest_framework import serializers
from pessoa.models import Pessoa

class PessoaApi(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id','nome','idade')
