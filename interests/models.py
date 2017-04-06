from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Interest(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	fb_accaount = models.URLField(blank=True)
	avatar = models.ImageField(upload_to='profile_images', blank=True)

	def __str__(self):
		return  self.user.username
		