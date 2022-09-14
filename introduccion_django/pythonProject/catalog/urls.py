from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("directores/", views.directores, name="directores"),
    path("peliculas/", views.peliculas, name="peliculas")
]