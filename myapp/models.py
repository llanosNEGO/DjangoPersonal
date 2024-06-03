from django.db import models

# Create your models here.

class Proyectos(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tareas (models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo