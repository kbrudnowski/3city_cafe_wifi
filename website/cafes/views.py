from django.shortcuts import render, redirect
from .models import Cafes
from .forms import CreateNewList
from django.contrib import messages

# Create your views here.


def home(response):
    cafes = Cafes.objects.all()
    return render(response, "cafes/home.html", {'cafes': cafes})


def add_cafe(response):
    if response.user.is_authenticated():
        if response.method == "POST":
            form = CreateNewList(response.POST)

            if form.is_valid():
                c = Cafes(
                    name=form.cleaned_data['name'],
                    photo=form.cleaned_data['photo'],
                    location=form.cleaned_data['location'],
                    g_rating=form.cleaned_data['g_rating'],
                    work_conditions=form.cleaned_data['work_conditions']
                )
                c.save()
                return redirect(home)
        else:
            form = CreateNewList()
        return render(response, "cafes/add.html", {'form': form})
    else:
        messages.info(response, 'You need to be logged in to add new cafes.')
        return redirect(home)
