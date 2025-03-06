from django.db import models
from django.utils.safestring import mark_safe

class Marca(models.Model):
    marca = models.CharField(max_length=50)
    def __str__(self):
        return self.marca

class Carousel(models.Model):
    nome = models.CharField(max_length=100)
    descrcao = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='carousel')
    def __str__(self):
        return self.nome
    @mark_safe
    def get_foto(self):
        if self.foto:
            return f'<img  width="50px" src="{self.foto.url}">'
        return "Sem foto"

class Carros(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    foto = models.ImageField(upload_to='carros', null=False, blank=False)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100, null=False, blank=False)
    ano = models.IntegerField(null=False, blank=False)
    valor = models.DecimalField(max_digits=15, decimal_places=0)
    descrição = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.nome
    
    @mark_safe
    def get_foto(self):
        if self.foto:
            return f'<img  width="50px" src="{self.foto.url}">'
        return "Sem foto"