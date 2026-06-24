from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from libro.models import Libro

from .forms import Mensaje
from .models import Comunicacion

@login_required
def nuevo_chat(request, libro_pk):
    libro = get_object_or_404(
        Libro.objects.select_related('creado_por'),
        pk=libro_pk
    )

    if libro.creado_por == request.user:
        return redirect('panel:index')

    comunicacion = Comunicacion.objects.filter(
        libro=libro, miembros=request.user
    ).first()

    if comunicacion:
        return redirect('comunicacion:detalles', pk=comunicacion.id)

    if request.method == 'POST':
        form = Mensaje(request.POST)
        if form.is_valid():
            comunicacion = Comunicacion.objects.create(libro=libro)
            comunicacion.miembros.add(request.user, libro.creado_por)

            mensaje = form.save(commit=False)
            mensaje.comunicacion = comunicacion
            mensaje.creado_por = request.user
            mensaje.save()

            return redirect('libro:detalles', pk=libro_pk)
    else:
        form = Mensaje()

    return render(request, 'comunicacion/nuevo.html', {'form': form})

@login_required
def bandeja_entrada(request):
    comunicacion = Comunicacion.objects.filter(
        miembros=request.user
    ).select_related('libro').prefetch_related('miembros')

    return render(request, 'comunicacion/bandeja.html', {
        'comunicacion': comunicacion
    })

@login_required
def detalles(request, pk):
    comunicacion = get_object_or_404(
        Comunicacion.objects.prefetch_related('mensajes__creado_por', 'miembros'),
        pk=pk, miembros=request.user
    )

    if request.method == 'POST':
        form = Mensaje(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.comunicacion = comunicacion
            mensaje.creado_por = request.user
            mensaje.save()
            return redirect('comunicacion:detalles', pk=pk)
    else:
        form = Mensaje()

    return render(request, 'comunicacion/detalles.html', {
        'comunicacion': comunicacion,
        'form': form
    })
