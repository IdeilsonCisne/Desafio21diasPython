from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
  resposta = {}
  resposta["conteudo"] = "Agora com conteúdo vindo do controller"
  return render(request, 'home/index.html', resposta)

def about(request):
  return render(request, 'home/about.html')

def contact(request):
  return render(request, 'home/contact.html')

def post(request):
  return render(request, 'home/post.html')

def html_bruto(request):
  return HttpResponse("<h1>Respondendo com html</h1>")

def json(request):
  resposta = {}
  resposta["conteudo"] = "Agora com API JSON"
  return JsonResponse(resposta)


def xml_bruto(request):
  xml_bruto = '<?xml version="1.0" encoding="UTF-8"?><bookstore><book category="cooking"><title lang="en">Everyday Italian</title><author>Giada De Laurentiis</author><year>2005</year><price>30.00</price></book></bookstore>'
  return HttpResponse(xml_bruto, content_type="text/xml")
