# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("A view Index funcionou, WOW!")

def sobre(request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvido por mim<h1>")

def contato(request):
    return HttpResponse("Esta é a página de contato.")

def ajuda(request):
    return HttpResponse("Esta é a página de ajuda")
