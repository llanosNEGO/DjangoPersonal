from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Proyectos,Tareas

# Create your views here.

def hello (request,usuario ):
    print(usuario)
    return HttpResponse ("<h1>Primera Fase con %s</h1>" %usuario)

def segunda(request):
    return HttpResponse ("<h1>Segunda Fase</h1>")

def Proyecto(request):
    proyecto = list(Proyectos.objects.values())
    return JsonResponse (proyecto , safe = False)

def Tarea(request, mensaje):
    mensaje = Tareas.objects.get(titulo = mensaje)   
    return HttpResponse(" titulo es: %s" %mensaje.titulo)