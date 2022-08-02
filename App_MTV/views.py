from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def Inicio(request):

    return render(request,"inicio.html")

def Sucursal(request):

    return render(request,"sucursal.html")


def Clientes(request):

    return render(request,"clientes.html")


def Comida(request):

    return render(request,"comida.html")


def Entrega(request):

    return render(request,"entrega.html")            