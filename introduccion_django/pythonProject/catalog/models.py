from django.db import models
from django.urls import reverse

class Director(models.Model):
    name = models.CharField(max_length=64, help_text="Nombre del director de cine")

    def __str__(self):
        return self.name


class Pelicula(models.Model):
    titulo = models.CharField(max_length=32)
    descripcion = models.TextField(max_length=100, help_text="Pon de que trata la película")
    director = models.ForeignKey("Director", on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.titulo

    def get_adsolute_url(self):
        return reverse("pelicula-detail", args=[str(self.id)])