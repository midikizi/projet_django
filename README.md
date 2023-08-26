# projet_django

Avant d'installer un projet Django, assurez-vous d'avoir les prérequis suivants :

Python : Django est écrit en Python, donc vous devez avoir Python installé sur votre système. Assurez-vous d'avoir Python 3.x installé.

Gestionnaire de paquets : Vous aurez besoin d'un gestionnaire de paquets Python pour installer Django et d'autres dépendances. Le gestionnaire de paquets standard est pip.

Environnement virtuel (recommandé) : Bien qu'il ne soit pas obligatoire, il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances de chaque projet. Vous pouvez utiliser virtualenv ou venv pour créer un environnement virtuel.

Une fois que vous avez satisfait ces prérequis, voici les étapes pour installer un projet Django :

Créez un environnement virtuel (facultatif) : Si vous choisissez d'utiliser un environnement virtuel, créez-en un dans le dossier de votre projet. Naviguez vers le dossier de votre projet dans le terminal et exécutez la commande suivante (en supposant que vous utilisez virtualenv):

sh
Copy code
virtualenv venv
Activez l'environnement virtuel : Selon votre système d'exploitation, activez l'environnement virtuel :

Sur Windows :

sh
Copy code
venv\Scripts\activate
Sur macOS et Linux :

sh
Copy code
source venv/bin/activate
Installez Django : Avec l'environnement virtuel activé, utilisez pip pour installer Django :

sh
Copy code
pip install django
Créez un projet Django : Une fois Django installé, créez un nouveau projet en utilisant la commande django-admin :

sh
Copy code
django-admin startproject nom_du_projet
Naviguez dans le dossier du projet : Accédez au dossier du projet nouvellement créé :

sh
Copy code
cd nom_du_projet
Lancez le serveur de développement : Démarrez le serveur de développement de Django avec la commande suivante :

sh
Copy code
python manage.py runserver
Accédez au projet dans votre navigateur : Ouvrez votre navigateur web et accédez à l'URL indiquée dans la sortie de la commande précédente (généralement http://127.0.0.1:8000/).

Votre projet Django est maintenant installé et fonctionne localement. Vous pouvez commencer à travailler sur votre application en ajoutant des applications, des modèles, des vues et des templates. N'oubliez pas de désactiver l'environnement virtuel lorsque vous avez terminé en utilisant la commande :

sh
Copy code
deactivate
Ces étapes vous permettront de mettre en place un projet Django de base. Vous devrez ensuite personnaliser et développer votre projet en fonction de vos besoins.
