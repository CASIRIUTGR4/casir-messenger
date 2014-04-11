from django.shortcuts import render

# Create your views here.
def index(request):
    
    context = {
               "message": "CASIR Messenger la messagerie éphémère !",
               "connexion":"Se connecter",
               "inscription": "Nouveau sur CASIR Messenger ?",
               }
    
    return render(request, "snapchat/index.html", context)

def dashboard(request):
    
    context = {
               "message" : "Dashboard :  Gestion des messages",
               }
    return render(request, "snapchat/dashboard.html", context)
