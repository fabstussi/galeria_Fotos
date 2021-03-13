from django.shortcuts import render
from .models import Categoria, Foto
# from django.http import HttpResponse


def galeria(request):
    categoria = Categoria.objects.all()
    fotos = Foto.objects.all().order_by('-data')
    return render(request, 'galeria/galeria.html', {'categorias': categoria, 'fotos': fotos})

def categoria(request, id):
    categoria = Categoria.objects.all()
    fotos = Foto.objects.filter(categoria__pk=id)
    return render(request, 'galeria/categoria.html', {'categorias': categoria, 'fotos': fotos})

def imagem(request, id):
    imagem = Foto.objects.filter(id=id).order_by('-data')
    return render(request, 'galeria/imagem.html', {'imagem': imagem[0]})
