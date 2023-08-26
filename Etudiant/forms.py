from django import forms
from .models import Soumission
from AppEcole.models import User

class SoumissionForm(forms.ModelForm):
    matiere = forms.CharField(label='matiere', widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg'
    }))
    projet = forms.CharField(label='Projet', widget=forms.FileInput(attrs={
        'class': 'form-control form-control-lg'
    }))
    

    class Meta:
        model = Soumission
        fields = ['matiere', 'projet']
        labels = {
            'matiere': 'matiere',
            'projet': 'projet',
            
        }
