from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NuevoLibro, EditarLibro
from .models import Libro, Categoria

def libros(request):
    consulta = request.GET.get('consulta', '')  
    categoria_id = request.GET.get('categoria', 0)  
    categorias = Categoria.objects.all()  
    libros = Libro.objects.filter(vendido=False) 

    if categoria_id:
        libros = libros.filter(categoria_id=categoria_id) 

    if consulta:
        libros = libros.filter(Q(nombre__icontains=consulta) | Q(descripción__icontains=consulta))

    return render(request, 'libro/libros.html', {
        'libros': libros,
        'consulta': consulta,
        'categorias': categorias,
        'categoria_id': int(categoria_id)
    })

def detalles(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    libros_relacionados = Libro.objects.filter(categoria=libro.categoria).exclude(pk=pk)[:3]
    
    context = {
        'libro': libro,
        'libros_relacionados': libros_relacionados
    }
    
    return render(request, 'libro/detalles.html', context)

@login_required 
def nuevo(request):
    if request.method == 'POST':
        form = NuevoLibro(request.POST, request.FILES) 

        if form.is_valid():
            libro = form.save(commit=False) 
            libro.creado_por = request.user 
            libro.save() 

            return redirect('libro:detalles', pk=libro.id) 
    else:
        form = NuevoLibro()  

    return render(request, 'libro/form.html', {
        'form': form,
        'title': 'Nuevo Libro',
    })

@login_required 
def editar(request, pk):
    libro = get_object_or_404(Libro, pk=pk, creado_por=request.user)  

    if request.method == 'POST':
        form = EditarLibro(request.POST, request.FILES, instance=libro)  

        if form.is_valid():
            form.save()

            return redirect('libro:detalles', pk=libro.id)
    else:
        form = EditarLibro(instance=libro)

    return render(request, 'libro/form.html', {
        'form': form,
        'title': 'Editar Libro',
    })

@login_required 
def eliminar(request, pk):
    libro = get_object_or_404(Libro, pk=pk, creado_por=request.user) 
    libro.delete() 

    return redirect('panel:index') 