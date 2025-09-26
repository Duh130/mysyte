from django.shortcuts import render
from django.http import HttpResponse  # ✅ Import necessário
from .utils import ler_arquivo_seguro

def minha_view(request):
    conteudo = ler_arquivo_seguro("teste.txt")
    return HttpResponse(conteudo)  # ✅ Agora funciona

def home(request):
    return render(request, "home.html")
