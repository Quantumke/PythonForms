from django.db import models


# Create your models here.
class forms(models.Model):
	username = models.CharField(max_length=100, unique=False)
	email = models.CharField(max_length=100, unique=False)
	school = models.CharField(max_length=100, unique=False)
	form = models.CharField(max_length=100, unique=False)
	date = models.CharField(max_length=100, unique=False)
	gender = models.CharField(max_length=100, unique=False)
	password = models.CharField(max_length=100, unique=False)
	def __unicode__(self):
		return '%s'%self.username
