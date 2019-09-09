from django import forms

from .models import Publicacion

class FormPub(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ('titulo', 'texto',)
