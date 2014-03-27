from django.shortcuts import render

# Create your views here.
def index(request):
    
    context = {
               "message": "Page d'accueil et d'authentification",
               }
    
    return render(request, "snapchat/index.html", context)