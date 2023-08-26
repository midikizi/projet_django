from django.urls import path
from .views import register,liste_utilisateur,modifier_utilisateur,supprimer_utilisateur,liste_cour,ajouter_cour,modifier_cour,supprimer_cour, liste_Enseignant, liste_Etudiant
urlpatterns = [
    path('user/ajouter', register, name='inscription'),
    path('user/', liste_utilisateur, name='liste_utilisateur'),
    path('user/enseignant', liste_Enseignant, name='liste_enseignant'),
    path('user/etudiant', liste_Etudiant, name='liste_etudiant'),
    path('user/modifier/<int:id>',modifier_utilisateur, name='modifier_utilisateur'),
    path('user/supprimer/<int:id>',supprimer_utilisateur, name='supprimer_utilisateur'),
    path('cour/ajouter', ajouter_cour, name='ajouter_cour'),
    path('cour/', liste_cour, name='liste_cour'),
    path('cour/modifier/<int:id>',modifier_cour, name='modifier_cour'),
    path('cour/supprimer/<int:id>',supprimer_cour, name='supprimer_cour'),
    
    
    
    
    
    


]
