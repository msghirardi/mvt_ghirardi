from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

from AppEntregable.models import Familiar

def crear_familiar(request):
    template = loader.get_template("template1.html")
    familia = Familiar(nombre = "Santiago", nacimiento = "2020-7-7", edad = "2")
    familia_2 = Familiar(nombre = "Marta", nacimiento = "1970-6-7", edad = "52")
    familia_3 = Familiar(nombre = "Ramon", nacimiento = "1966-8-9", edad = "56")

    dict_de_contexto = {
        "familia_1":familia.nombre,
        "familia_2":familia_2.nombre,
        "familia_3":familia_3.nombre,
       
    }
    
    res = template.render(dict_de_contexto)

    
    return HttpResponse(res)
