from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.CharField(max_length=100)
    myteam = 'SJSU'

    def __str__(self):
    	return self.user