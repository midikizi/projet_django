from django.urls import path
from .views import liste_Projets,ajouter_soumission,liste_soumission,modifier_soumission,supprimer_soumission, afficher_profil,modifier_profil
urlpatterns = [
    path('projets/', liste_Projets, name='etudiants_projet'),
    path('soumission/ajouter', ajouter_soumission, name='ajouter_soumission'),
    path('soumission/',liste_soumission, name='liste_soumission'),
    path('soumission/modifier/<int:id>', modifier_soumission, name='modifier_soumission'),
    path('soumission/supprimer/<int:id>', supprimer_soumission, name='supprimer_soumission'),
    path('profil/', afficher_profil, name='profil'),
    path('profil/modifier/<int:id>', modifier_profil, name='profil_modifier'),

]
