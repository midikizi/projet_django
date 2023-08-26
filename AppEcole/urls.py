from django.urls import path
from .views import index, inscription, connexion,ajouter_projet,deconnexion,liste_projets,modifier_projet,supprimer_projet,afficher_profil,modifier_profil,liste_projets_soumis
urlpatterns = [
    path('acceuil', index, name='acceuil'),
    path('inscription/', inscription, name='register'),
    path('', connexion, name='login'),
    path('deconnexion/', deconnexion, name='logout'),
    
    
    path('enseignant/projet/ajouter', ajouter_projet, name='ajouter_projet'),
    path('enseignant/projet/', liste_projets, name='liste_projet'),
    path('enseignant/projet/modifier/<int:id>',modifier_projet, name='modifier_projet'),
    path('enseignant/projet/supprimer/<int:id>',supprimer_projet, name='supprimer_projet'),
    path('enseignant/profil',afficher_profil, name='afficher_profil'),
    path('enseignant/profil/modifier/<int:id>',modifier_profil, name='modifier_profile'),
    path('enseignant/projet/soumis',liste_projets_soumis, name='soumis'),


]
