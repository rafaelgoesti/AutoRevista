from django.contrib import admin
from .models import Carousel, Carros, Marca
from django_object_actions import DjangoObjectActions

class MarcaCarrosAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca',)

class CarouselHeaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'get_foto',)
    list_display_links = ('id', 'nome',)
    search_fields = ('id', 'nome',)

class CarouselBodyAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'marca', 'modelo', 'ano', 'valor', 'get_foto',)
    list_display_links = ('id', 'nome', 'marca', 'modelo',)
    search_fields = ('id', 'nome', 'marca', 'modelo',)

admin.site.register(Marca, MarcaCarrosAdmin)
admin.site.register(Carousel, CarouselHeaderAdmin)
admin.site.register(Carros, CarouselBodyAdmin)
