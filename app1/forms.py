from django import forms
from .models import Auau


class formulario_RH(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    texto = forms.CharField(widget = forms.Textarea)


class formulario_Auau(forms.ModelForm):
    class Meta:
        model = Auau
        fields = '__all__'


