from django.urls import path
from App_MTV import views
from App_MTV.views import Inicio,Entrega,Comida,Clientes


urlpatterns = [
    path('', views.Inicio),
    path('entrega', views.Entrega,),
    path('comida', views.Comida),
    path('clientes', views.Clientes),
    
]
