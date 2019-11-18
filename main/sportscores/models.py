from django.db import models

# Create your models here.

class teams(models.Model):
	team_id = models.IntegerField(primary_key=True)
	teamName = models.CharField(max_length=100)
	teamImage = models.ImageField(upload_to='team')

	def __str__(self):
		return self.teamName