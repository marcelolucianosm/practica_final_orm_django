from django import forms

from .models import Laboratorio


class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['laboratorio', 'ciudad', 'pais']
        widgets = {
            'laboratorio': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
        }