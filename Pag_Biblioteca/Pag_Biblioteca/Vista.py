'''
Created on Jun 7, 2017

@author: curso
'''
'''from django.template.context_processors import request
from django.template.context_processors import request'''

from django.shortcuts import render

def inicio(request):
    return render(request, 'Saludo_2.html')
def reservar(request):
    return render(request, 'reservar.html')
def borrar(request):
    return render(request, 'borrar.html')
def ingresar(request):
    return render(request, 'ingresar.html')
def pedir(request):
    return render(request, 'pedir.html')
def registrar(request):
    return render(request, 'registrar.html')
def ver(request):
    return render(request, 'ver.html')

    
    
    
    
    
    
    