from django.shortcuts import render,redirect,get_object_or_404
from django.core.validators import validate_email
from AppEcole.models import User
from Administrateur.models import Cour
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import CourForm
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.role == 'Administrateur'




@user_passes_test(is_admin, login_url='login')
def register(request):
    error = False
    message = ""
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        password = request.POST.get('password')
        confirmePassword = request.POST.get('confirmePassword')
        role = request.POST.get('role')
        identifiant = request.POST.get('identifiant')
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
            return redirect('liste_utilisateur')
            
    context = {
        'error': error,
        'message': message
    }
    return render(request, 'administrateur/users/inscription.html', context)   

@user_passes_test(is_admin, login_url='login')
def liste_Etudiant(request):
    users = User.objects.filter(role='Etudiant')
    
    return render(request, 'administrateur/users/utilisateur_etudiant.html', {'users': users}) 

@user_passes_test(is_admin, login_url='login')
def liste_Enseignant(request):
    users = User.objects.filter(role='Enseignant')  
    return render(request, 'administrateur/users/utilisateur_enseignant.html', {'users': users}) 

@user_passes_test(is_admin, login_url='login')
def liste_utilisateur(request):
    users = User.objects.filter(Q(role='Enseignant') | Q(role='Etudiant'))  
    return render(request, 'administrateur/users/utilisateur.html', {'users': users}) 

@user_passes_test(is_admin, login_url='login')
def modifier_utilisateur(request, id):
    error = False
    message = ""
    user = get_object_or_404(get_user_model(), id=id)  # Get the user object or return 404 if not found
    
    if request.method == "POST":
        # Similar to your existing code to retrieve form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        password = request.POST.get('password')
        confirmePassword = request.POST.get('confirmePassword')
        role = request.POST.get('role')
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
            return redirect('liste_utilisateur')  # Redirect to user list page after successful update

    context = {
        'user': user,
        'error': error,
        'message': message
    }
    return render(request, 'administrateur/users/modifier.html', context)

@user_passes_test(is_admin, login_url='login')
def supprimer_utilisateur(request, id):
    messages=""
    user = get_object_or_404(get_user_model(), id=id)
    username=user.username
    
    if request.method == 'POST':
        user.delete()
        return redirect('liste_utilisateur')  # Rediriger vers la liste des projets
        messages="votre utilisateur a été supprimer avec succes" 
    context = {'user': user,
               'username':username,
               'message':messages}
    return render(request, 'administrateur/users/supprimer.html', context)







@user_passes_test(is_admin, login_url='login')
def ajouter_cour(request):
    messages= ''
    if request.method == 'POST':
        form = CourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form=CourForm()
            messages = "votre Cour a été ajouter avec succes" # Rediriger vers la liste des projets
    else:
        form = CourForm()
    
    context = {'form': form,'message' :messages} 
    return render(request, 'administrateur/cours/ajouter.html', context)

@user_passes_test(is_admin, login_url='login')
def liste_cour(request):
    cours = Cour.objects.all()
    return render(request, 'administrateur/cours/index.html', {'cours': cours})

@user_passes_test(is_admin, login_url='login')
def modifier_cour(request, id):
    cour = get_object_or_404(Cour, id=id)
    messages=""
    if request.method == 'POST':
        form = CourForm(request.POST, request.FILES, instance=cour)
        if form.is_valid():
            form.save()
            form=CourForm
            messages="votre Cour a été modifier avec succes"
            
            
             # Rediriger vers la liste des projets
    else:
        form = CourForm(instance=cour)
    
    context = {'form': form,
               'message':messages}
    return render(request, 'administrateur/cours/modifier.html', context)

@user_passes_test(is_admin, login_url='login')
def supprimer_cour(request, id):
    messages=""
    cour = get_object_or_404(Cour, id=id)
    intitule=cour.intitule
    
    if request.method == 'POST':
        cour.delete()
        return redirect('liste_cour')  # Rediriger vers la liste des projets
        messages="votre cour a été supprimer avec succes" 
    context = {'intitule': intitule,
               'cour':cour,
               'message':messages}
    return render(request, 'administrateur/cours/supprimer.html', context)




# Create your views here.
