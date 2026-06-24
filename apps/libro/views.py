from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NuevoLibro, EditarLibro
from .models import Libro, Categoria

def libros(request):
    consulta = request.GET.get('consulta', '')
    categoria_id = request.GET.get('categoria', 0)
    orden = request.GET.get('orden', '')

    categorias = Categoria.objects.all()
    libros_list = Libro.objects.filter(vendido=False).select_related('categoria', 'creado_por')

    if categoria_id:
        categoria_id = int(categoria_id)
        libros_list = libros_list.filter(categoria_id=categoria_id)

    if consulta:
        libros_list = libros_list.filter(
            Q(nombre__icontains=consulta) | Q(descripcion__icontains=consulta)
        )

    if orden == 'precio_asc':
        libros_list = libros_list.order_by('precio')
    elif orden == 'precio_desc':
        libros_list = libros_list.order_by('-precio')
    else:
        libros_list = libros_list.order_by('-creado_en')

    paginator = Paginator(libros_list, 20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'libro/libros.html', {
        'page_obj': page_obj,
        'consulta': consulta,
        'categorias': categorias,
        'categoria_id': categoria_id,
        'orden': orden,
    })

def detalles(request, pk):
    libro = get_object_or_404(
        Libro.objects.select_related('categoria', 'creado_por'),
        pk=pk
    )
    libros_relacionados = Libro.objects.filter(
        categoria=libro.categoria
    ).exclude(pk=pk).select_related('categoria')[:4]

    return render(request, 'libro/detalles.html', {
        'libro': libro,
        'libros_relacionados': libros_relacionados,
    })

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
    libro.activo = False
    libro.save()
    return redirect('panel:index')
