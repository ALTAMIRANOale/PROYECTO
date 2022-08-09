from django.urls import path
from . import views

"""la url empieza con Noticias/(el nombre de estearchivo)"""
app_name = 'noticias'
urlpatterns = [
    
    path('listar/', views.listar, name = 'listar_noticias'),
]
