from django.shortcuts import render
from . import forms
from .forms import Formulario_RH, formulario_Auau
from app1.models import Auau

# Create your views here.
def index(request):
    dic = {'complemento': "Sou a função index (view inicial) - Home Page!"}
    return render(request, 'templates01/first.html', context=dic)

def index_app1(request):
    dic = {'complemento': "Sou a função index (view inicial) criada no app1"}
    return render(request, 'templates01/first.html', context=dic)

def tela01_app1(request):
    dic = {'complemento': "Olá, eu sou a view 'tela01_app1. Pronta para receber html, js e css"}
    return render(request, 'templates01/first.html', context=dic)

def index_atividade(request):
    dic = {'link_index': 'Venha aprender Python'}
    return render(request, 'templates01/index_atividade.html', context=dic)

def help(request):
    dic = {'link_01': 'Pandas', 'link_02': 'seaborn', 'link_03': 'statsmodels'}
    return render(request, 'templates01/help.html', context=dic)

def turismo(request):
    return render(request, 'templates01/turismo.html')

def calculadora(request):
    return render(request, 'templates01/calculadora.html')

def formulario_rh_view(request):
    formulario = forms.Formulario_RH()
    if request.method == 'post':
        formulario = forms.Formulario_RH(request.POST)
        if formulario.is_valid():
            print(f'Formulario validado pelo método POST')
    return render(request, 'templates01/formulario_rh.html', {'formulario': formulario})

def form_auau(request):
    formulario = formulario_Auau
    if request.method == 'POST':
        formulario = formulario_Auau(request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            print("Vish, deu errado")
    return render(request, 'templates01/formulario_model_Auau.html', {'formulario_auau': formulario})


