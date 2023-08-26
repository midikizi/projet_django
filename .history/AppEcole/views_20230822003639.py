from django.shortcuts import render,redirect,get_object_or_404
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import ProjetForm
from django.contrib.auth import get_user_model
from .models import Devoir
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from Etudiant.models import Soumission

def is_enseignant(user):
    return user.role == 'Enseignant'

def is_not_authenticated(user):
    return not user.is_authenticated







def index(request):
    return render(request,'index.html')


@user_passes_test(is_enseignant, login_url='login')
def ajouter_projet(request):
    messages= ''
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form=ProjetForm()
            messages = "votre projet a été ajouter avec succes" # Rediriger vers la liste des projets
    else:
        form = ProjetForm()
    
    context = {'form': form,'message' :messages} 
    return render(request, 'Enseignant/Projet/projet.html', context)

@user_passes_test(is_enseignant, login_url='login')
def liste_projets(request):
    projets = Devoir.objects.all()
    return render(request, 'Enseignant/Projet/index.html', {'Projets': projets})

@user_passes_test(is_enseignant, login_url='login')
def modifier_projet(request, id):
    projet = get_object_or_404(Devoir, id=id)
    messages=""
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES, instance=projet)
        if form.is_valid():
            form.save()
            form=ProjetForm
            messages="votre projet a été modifier avec succes"
            
            
             # Rediriger vers la liste des projets
    else:
        form = ProjetForm(instance=projet)
    
    context = {'form': form,
               'message':messages}
    return render(request, 'Enseignant/Projet/modifier.html', context)


@user_passes_test(is_enseignant, login_url='login')
def supprimer_projet(request, id):
    messages=""
    projet = get_object_or_404(Devoir, id=id)
    intitule=projet.intitule
    
    if request.method == 'POST':
        projet.delete()
        return redirect('liste_projet')  # Rediriger vers la liste des projets
        messages="votre projet a été supprimer avec succes" 
    context = {'intitule': intitule,
               'projet':projet,
               'message':messages}
    return render(request, 'Enseignant/Projet/supprimer.html', context)

@user_passes_test(is_enseignant, login_url='login')
def modifier_profil(request, id):
    error = False
    message = ""
    user = request.user  # Get the user object or return 404 if not found
    
    if request.method == "POST":
        # Similar to your existing code to retrieve form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        password = request.POST.get('password')
        confirmePassword = request.POST.get('confirmePassword')
        role = "Enseignant"
        identifiant = request.POST.get('identifiant')
        date = request.POST.get('date')
        image = request.POST.get('image')

        try:
            validate_email(email)
        except:
            error = True
            message = "Entrer un email valide svp"

        existing_user = get_user_model().objects.filter(Q(email=email) | Q(username=username)).exclude(id=id).first()
        if existing_user:
            error = True
            message = f"L'email {email} ou le nom d'utilisateur {nom} est déjà utilisé par un utilisateur"

        if password and password != confirmePassword:
            error = True
            message = "Les deux mots de passe ne sont pas identiques"

        if not error:
            # Update user data
            user.username = username
            user.email = email
            user.last_name = nom
            user.first_name = prenom
            user.identifiant = identifiant
            user.role = role
            user.birthdate = date
            user.profil = image
            
            if password:
                user.set_password(password)  # Only set password if a new password is provided
            
            user.save()
            return redirect('login')  # Redirect to user list page after successful update

    context = {
        'user': user,
        'error': error,
        'message': message
    }
    return render(request, 'Enseignant/modifier.html', context)

@user_passes_test(is_enseignant, login_url='login')
def liste_projets_soumis(request):
   
    soumission = Soumission.objects.all()
    context = {'soumissions':soumission}
    return render(request, 'Enseignant/Projet/soumis.html', context)






def inscription(request):
    error = False
    message = ""
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        password = request.POST.get('password')
        confirmePassword=request.POST.get('confirmePassword')
        role = "Administrateur"
        identifiant ="admin"
        date = request.POST.get('date')
        image = request.POST.get('image')
        # Récupérer le rôle du formulaire
        
        try:
            validate_email(email)
        except:
            error = True
            message = "Entrer un email valide svp"
            
        User = get_user_model()  # Obtenir le modèle utilisateur personnalisé
        
        user = User.objects.filter(Q(email=email) | Q(username=username)).first()
        if user:
            error = True
            message = f"L'email {email} ou le nom d'utilisateur {nom} est déjà utilisé par un utilisateur"
            
        if password != confirmePassword:
            error = True
            message = "Les deux mots de passe ne sont pas identiques"
            
        if error == False:
            user = User(
                
                username=username,
                email=email,
                last_name=nom,
                first_name=prenom,
                identifiant=identifiant,
                role=role,
                birthdate=date,
                profil=image# Enregistrer le rôle dans le modèle
            )
            user.set_password(password)
            user.save()
            return redirect('login')
            
    context = {
        'error': error,
        'message': message
    }
    return render(request, 'Utilisateur/inscription.html', context)

@login_required
def afficher_profil(request):
        utilisateur = request.user
        return render(request, 'Enseignant/profil.html', {'utilisateur': utilisateur})


def connexion(request):
    if request.user.is_authenticated:
        logout(request)
    
    error=False
    messages=""
    if request.method=="POST":
      
        email=request.POST.get('email', None)
        password=request.POST.get('password', None)
        
        User = get_user_model() 
        user=User.objects.filter(email=email).first()
        if user:
            user=authenticate(username=user.username, password=password)
            if user:
                login(request, user)
                if user.role == 'Administrateur':
                    return redirect('liste_utilisateur')  # Redirection pour les superutilisateurs
                elif user.role == 'Enseignant':
                    return redirect('liste_projet')  # Redirection pour les membres du groupe "Staff"
                elif user.role == 'Etudiant':
                    return redirect('etudiants_projet')  
                else:
                    return redirect('acceuil')  # Redirection par défaut
               
            else: 
                error=True
                message="mot de passe  incorrecte"  
        else:        
            error=True
            message="l'utilisateur n'existe pas"  
    return render(request, 'Utilisateur/connexion.html', {'error':error, 'message':messages})     




def deconnexion(request):
    logout(request)  
    return redirect('login') 
# Create your views here.
