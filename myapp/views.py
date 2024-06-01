from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello (request):
    return HttpResponse ("<h1>Primera Fase</h1>")

def segunda(request):
    return HttpResponse ("<h1>Segunda Fase</h1>")