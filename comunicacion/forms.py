from django import forms

from .models import Mensaje

class Mensaje(forms.ModelForm):
    class Meta:
        model = Mensaje
        
        fields = ('contenido',)
        
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 dark:bg-gray-900 rounded-sm border dark:border-none border-gray-300 focus:outline-none border-solid focus:border-dashed resize-none'
                })
        }