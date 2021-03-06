from django.db import models
from django.contrib.auth.models import User

#Create your models here.
       
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
    invitation = models.BooleanField()
