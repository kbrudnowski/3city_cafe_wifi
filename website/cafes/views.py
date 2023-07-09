from django.shortcuts import render
from .models import Cafes

# Create your views here.


def home(response):
    cafes = Cafes.objects.all()
    return render(response, "cafes/home.html", {'cafes': cafes})


def index(response):
    return render(response, "cafes/base.html")
