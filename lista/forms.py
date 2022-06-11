from django import forms
from .models import Lista

class ListaForms(forms.ModelForm):
    class Meta:
        model = Lista
        fields = '__all__'
        labels = {'nome_item':'Nome', 'quantidade':'Quantidade', 'valor':'Valor por item', 'observacao':'Observação'}
    