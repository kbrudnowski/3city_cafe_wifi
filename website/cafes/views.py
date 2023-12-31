from django.shortcuts import render, redirect
from .models import Cafes
from .forms import CreateNewList


def home(response):
    cafes = Cafes.objects.all()
    return render(response, "cafes/home.html", {'cafes': cafes})


def add_cafe(response):
    if response.user.is_authenticated:
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
        return redirect(home)


def delete_cafe(response, id):
    Cafes.objects.all().get(id=id).delete()
    return redirect(home)
