# -*- coding: utf-8 -*-
from django.shortcuts import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):

    context = {
               "message": "CASIR Messenger la messagerie éphémère",
               "connexion": "Se connecter",
               "inscription": "Nouveau sur CASIR Messenger ?",
               }
    
    if request.POST:
        if 'connection' in request.POST:
            username = request.POST['c_username']
            password = request.POST['c_password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("snapchat/dashboard")
                else:
                    error = {"disable_account": "Ce compte est désactivé !"}
                    context.update(error)
                    return render(request, "snapchat/index.html", context)
            else:
                error = {"wrong_logins": "Vos identifiants sont incorrects !"}
                context.update(error)
            
        elif 'registration' in request.POST:
            user = User(name=request.POST['r_username'],password=request.POST['r_password'],email=request.POST['r_mail'])
            user.save
            inscription = {"inscription": "Votre compte a bien été créé, vous pouvez maintenant vous connecter"}
            context.update(inscription)
  
    return render(request, "snapchat/index.html", context)
    

def dashboard(request):
    
    context = {
               "message" : "Dashboard :  Gestion des messages",
               }
    return render(request, "snapchat/dashboard.html", context)
