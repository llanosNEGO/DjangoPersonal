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
    #proyecto = list(Proyectos.objects.values())
    proyecto = Proyectos.objects.all()
    return render(request, 'proyecto.html' , {
        'proyectos':proyecto
    })

def Tarea(request):
    #mensaje = Tareas.objects.get(titulo = mensaje)   
    mensaje = 'Pendiente desarrollar fronted para POO'
    return render(request, 'tarea.html' , {
        'mensaje' : mensaje

    })

def index(request):
    return render(request, 'index.html')