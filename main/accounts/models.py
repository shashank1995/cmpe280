from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    #user = models.CharField(max_length=100)
    #user = models.ForeignKey(User)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #mysport1 = models.CharField(max_length=100)
    #mysport2 = models.CharField(max_length=100)
    Sport = models.CharField(max_length=100)
    Team = models.CharField(max_length=100)
    #language = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    
    def __str__(self):
    	return self.user.username
