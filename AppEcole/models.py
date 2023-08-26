from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    ETUDIANT= " ETUDIANT"
    ENSEIGNANT="ENSEIGNANT"
    ADMINISTRATEUR=" ADMINISTRATEUR"
    
    ROLE_CHOICES = (
        (ETUDIANT, 'Etudiant'),
        (ENSEIGNANT, 'Enseignant'),
        (ADMINISTRATEUR, 'Administrateur'),
    )
    
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    birthdate = models.DateField(null=True, blank=False)
    identifiant = models.CharField(max_length=20, null=True, blank=False)
    profil = models.ImageField( upload_to='projets', height_field=None, width_field=None, max_length=None, default="12.png", blank=True)

    def __str__(self):
        return self.username

class Devoir(models.Model):
    
    STATUT_CHOICES = [
        ('en_cours', 'En cours'),
        ('soumis', 'Soumis'),
        ('corrigé', 'Corrige'),
        ('traité', 'Traite'),
        ('archivé', 'Archivé'),
    ]
    intitule=models.CharField(max_length=255)
    matiere=models.CharField(max_length=255)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    projet = models.FileField(upload_to='projets')
    
    
    def __str__(self):
        return self.intitule
    
    
# Create your models here.
