from django.db import models
from django.contrib.auth import get_user_model

class Soumission(models.Model):
    matiere = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    projet = models.FileField(upload_to='projets')
    
    

    def __str__(self):
        return f"Soumission by {self.user.username} - {self.matiere}"

# Create your models here.
