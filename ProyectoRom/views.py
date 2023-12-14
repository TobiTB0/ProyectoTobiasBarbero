from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render


def roms(xx):
  
    
    diccionario = {}
    
    
    plantilla = loader.get_template('Roms.html')
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)
def emuladores(xx):
   
    
    diccionario = {}
    
    
    plantilla = loader.get_template('Emuladores.html')
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)
def login(xx):
   
    
    diccionario = { }
    
    
    plantilla = loader.get_template('login.html')
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)



def home(xx):
    
    
    diccionario = { }
    # html = open("C:/Users/Usuario/Documents/.programacion/Python1/ProyectoFinalRoms/ProyectoRom/ProyectoRom/Plantilla/template1.html")
    # plantilla = Template(html.read())
    
    # html.close()
    # contexto = Context(diccionario)
    plantilla = loader.get_template('Home.html')
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)


