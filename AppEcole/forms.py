from django import forms
from .models import Devoir

class ProjetForm(forms.ModelForm):
    intitule = forms.CharField(label='Intitulé', widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg'
    }))
    matiere = forms.CharField(label='Matière', widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg'
    }))
    projet = forms.FileField(label='Projet (Fichier)', widget=forms.ClearableFileInput(attrs={
        'class': 'form-control-file  form-control-lg'
    }))
    statut = forms.ChoiceField(label='Statut', choices=Devoir.STATUT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control form-control-lg'
    }))

    class Meta:
        model = Devoir
        fields = ['intitule', 'matiere', 'projet', 'statut']
