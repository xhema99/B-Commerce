from django import forms
from .models import Libro

INPUT_CLASSES = 'input'

class NuevoLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('categoria', 'nombre', 'descripcion', 'precio', 'imagen')
        widgets = {
            'categoria': forms.Select(attrs={'class': INPUT_CLASSES}),
            'nombre': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'descripcion': forms.Textarea(attrs={'class': INPUT_CLASSES, 'rows': 4}),
            'precio': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'imagen': forms.FileInput(attrs={'class': INPUT_CLASSES}),
        }

class EditarLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('nombre', 'descripcion', 'precio', 'imagen', 'vendido')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'descripcion': forms.Textarea(attrs={'class': INPUT_CLASSES, 'rows': 4}),
            'precio': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'imagen': forms.FileInput(attrs={'class': INPUT_CLASSES}),
        }
