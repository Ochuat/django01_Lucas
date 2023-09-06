from django import forms

class Formulario_RH(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    texto = forms.CharField(widget = forms.Textarea)

