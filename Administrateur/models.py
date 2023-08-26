from django.db import models
from django.contrib.auth import get_user_model

class Cour(models.Model):
    intitule = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    enseignant = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'Enseignant'},
        related_name='cours_enseignant'
    )

    def __str__(self):
        return self.intitule


# Create your models here.
