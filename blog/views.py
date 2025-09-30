from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def post_hello(request):
    return HttpResponse("Olá, esta é a página hello!")
