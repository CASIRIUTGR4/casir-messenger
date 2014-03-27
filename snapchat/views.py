from django.shortcuts import render

# Create your views here.
def index(request):
    
    context = {
               "message": "Page d'accueil et d'authentification",
               "connexion":"Zone de connexion",
               "inscription": "Zone d'inscription",
               }
    
    return render(request, "snapchat/index.html", context)