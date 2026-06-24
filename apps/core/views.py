from django.shortcuts import render, redirect
from libro.models import Categoria, Libro
from .forms import CrearcuentaForm

def index(request):
    libros = Libro.objects.filter(vendido=False).select_related('categoria').order_by('-creado_en')[:6]
    categorias = Categoria.objects.all()
    return render(request, 'core/index.html', {'categorias': categorias, 'libros': libros})

def contacto(request):
    return render(request, 'core/contacto.html')

def crearcuenta(request):
    if request.method == 'POST':
        form = CrearcuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = CrearcuentaForm()

    return render(request, 'core/crearcuenta.html', {'form': form})
