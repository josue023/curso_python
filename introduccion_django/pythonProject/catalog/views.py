from django.shortcuts import render

from .models import Director, Pelicula

def index(request):
    num_director = Director.objects.all().count()
    num_pelicula = Pelicula.objects.all().count()



    return render(
        request,
        "index.html",
        context={
            "num_director": num_director,
            "num_pelicula": num_pelicula
        }
    )


def directores(request):
    name_director = Director.objects.all()

    return render(
        request,
        "directores.html",
        context={
            "name_director": name_director,
        }
    )


def peliculas(request):
    name_pelicula = Pelicula.objects.all()

    return render(
        request,
        "peliculas.html",
        context={
            "name_pelicula": name_pelicula,
        }
    )