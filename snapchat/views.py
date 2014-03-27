from django.shortcuts import render

# Create your views here.
def index(request):
    
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
