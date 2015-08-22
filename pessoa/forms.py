from django import forms
from pessoa.models import Pessoa

class PessoaFormulario(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
