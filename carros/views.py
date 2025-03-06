from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .models import Carousel, Carros, Marca

def home(request):
    carros = Carros.objects.all()
    carousel = Carousel.objects.all()
    return render(request, 'index.html', {'carros': carros, 'carousel': carousel})

def buscar_marca(request):
    query = request.GET.get('search', '')
    print(f"Busca por: {query}")
    carros = Carros.objects.filter(marca__marca__icontains=query)
    print(f"Carros encontrados: {carros.count()}")

    return render(request, 'buscar.html', {'carros': carros})