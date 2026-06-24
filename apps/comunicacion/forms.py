from django import forms

from .models import Mensaje

class Mensaje(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ('contenido',)
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'input flex-1',
                'rows': 2,
                'placeholder': 'Escribí tu mensaje...'
            })
        }
