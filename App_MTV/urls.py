from django.urls import path
from App_MTV import views
from App_MTV.views import Inicio,Entrega,Comida,Clientes


urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('entrega', views.Entrega, name="Entrega"),
    path('comida', views.Comida, name="Comida"),
    path('clientes', views.Clientes,name="Clientes"),
    
]
