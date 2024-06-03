
from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello),
    path('segunda/', views.segunda),
    path('hello/<str:usuario>', views.hello),
    path('proyectos/',views.Proyecto),
    path('tarea/<str:mensaje>',views.Tarea),


]