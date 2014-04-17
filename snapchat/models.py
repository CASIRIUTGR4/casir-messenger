from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
=======

#Create your models here.
>>>>>>> 2b4a9f84fc7cb5ce781a48865d7d37765d3f0639
       
class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    sender = models.ForeignKey(User, related_name='sender')
    recever = models.ForeignKey(User, related_name='recever')
    message = models.CharField(max_length=100)
    attachment = models.ImageField(upload_to='photos')
    duration = models.TimeField()
    created = models.DateField()
       
class Friend(models.Model):
    idDemande = models.ForeignKey(User, related_name='demande')
    idFriend = models.ForeignKey(User, related_name='friend')
<<<<<<< HEAD
    invitation = models.BooleanField()
=======
    invitation = models.BooleanField()
>>>>>>> 2b4a9f84fc7cb5ce781a48865d7d37765d3f0639
