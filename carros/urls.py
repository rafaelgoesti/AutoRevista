from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('buscar/', views.buscar_marca, name='buscar_marca')
]
