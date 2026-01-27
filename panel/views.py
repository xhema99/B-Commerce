from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from libro.models import Libro

@login_required  
def index(request):
    libros = Libro.objects.filter(creado_por=request.user)

    return render(request, 'panel/index.html', {
        'libros': libros,
    })
