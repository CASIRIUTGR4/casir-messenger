from django.shortcuts import render
from django.contrib.auth import authenticate, login

def index(request):
    if request.POST:
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=login, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'snapchat/dashboard.html')
            else:
                context = {
                           "disable_account": "Ce compte est désactivé !"
                           }
        else:
            context = {
                       "wrong_logins": "Vos identifiants sont erronés !"
                       }
        
        context = {
                   "message": "Page d'accueil et d'authentification",
                   "connexion":"Zone de connexion",
                   "inscription": "Zone d'inscription",
                   }
        
        return render(request, "snapchat/index.html", context)

def dashboard(request):
    
    context = {
               "message" : "Dashboard :  Gestion des messages",
               }
    return render(request, "snapchat/dashboard.html", context)
