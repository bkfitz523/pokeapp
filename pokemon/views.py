from django.shortcuts import render
from django.http import HttpResponse
import pokemon.models

# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


# def TypeView(request):
#     query_results = pokemon.models.Type.objects.all()
