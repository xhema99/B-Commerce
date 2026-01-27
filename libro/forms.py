from django import forms
from .models import Libro

INPUT_CLASSES = 'w-full py-4 px-32 rounded-xl border'

class NuevoLibro(forms.ModelForm):
    class Meta:
        model = Libro  
        fields = ('categoria', 'nombre', 'descripción', 'precio', 'imagen') 

        widgets = {
            'categoria': forms.Select(attrs={
                'class': INPUT_CLASSES 
            }),
            'nombre': forms.TextInput(attrs={
                'class': INPUT_CLASSES 
            }),
            'descripción': forms.Textarea(attrs={
                'class': INPUT_CLASSES 
            }),
            'precio': forms.TextInput(attrs={
                'class': INPUT_CLASSES 
            }),
            'imagen': forms.FileInput(attrs={
                'class': INPUT_CLASSES 
            })
        }

class EditarLibro(forms.ModelForm):
    class Meta:
        model = Libro 
        fields = ('nombre', 'descripción', 'precio', 'imagen', 'vendido')  

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': INPUT_CLASSES  
            }),
            'descripción': forms.Textarea(attrs={
                'class': INPUT_CLASSES  
            }),
            'precio': forms.TextInput(attrs={
                'class': INPUT_CLASSES 
            }),
            'imagen': forms.FileInput(attrs={
                'class': INPUT_CLASSES 
            })
        }