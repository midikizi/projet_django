from django import forms
from .models import Cour
from AppEcole.models import User

class CourForm(forms.ModelForm):
    intitule = forms.CharField(label='Intitulé', widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg'
    }))
    code = forms.CharField(label='Code', widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg'
    }))
    enseignant = forms.ModelChoiceField(label='Enseignant', queryset=User.objects.filter(role='Enseignant'), widget=forms.Select(attrs={
        'class': 'form-control form-control-lg'
    }))

    class Meta:
        model = Cour
        fields = ['intitule', 'code', 'enseignant']
        labels = {
            'intitule': 'Intitulé',
            'code': 'Code',
            'enseignant': 'Enseignant',
        }
