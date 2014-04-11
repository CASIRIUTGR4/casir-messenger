from django.db import models

# Create your models here.
# class User(models.Model):
#     id = models.IntegerField(primary_key=True)
#     login = models.CharField(max_length=25)
#     password = models.CharField(max_length=20)
#     mail = models.EmailField(unique=true)
#      
# class Message(models.Model):
#     id = models.IntegerField(primary_key=True)
#     sender = models.ForeignKey('User')
#     recever = models.ForeignKey('User')
#     message = models.CharField(max_length=100)
#     attachment = models.ImageField()
#     duration = models.TimeField()
#     created = models.DateField()
#      
# class Friend(models.Model):
#     idDemande = models.ForeignKey('User')
#     idFriend = models.ForeignKey('User')
#     invitation = models.BooleanField()