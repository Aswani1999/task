from django import forms
from .models import formmodel

class bankform(forms.ModelForm):
    class Meta:
        model = formmodel
        exclude = []
