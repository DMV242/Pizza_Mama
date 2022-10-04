from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
# Create your views here.


def index(request):
   '''pizzas = Pizza.objects.all()
    pizzas_noms = [pizza.noms + " : " + str(pizza.prix) for pizza in pizzas]
    pizzas_noms_str = ", ".join(pizzas_noms)
    return HttpResponse("Les pizzas " + pizzas_noms_str)'''
   pizzas = Pizza.objects.all().order_by('noms')
   return render(request, 'menu/index.html',{"pizzas": pizzas})