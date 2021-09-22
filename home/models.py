from django.db import models


# Create your models here.

class contact(models.Model):
	name 		= models.CharField(max_length=255)	
	email 		= models.EmailField(max_length=254)
	phone 		= models.CharField(max_length=13)
	subject 	= models.TextField(max_length=80, blank=False)
	content 	= models.TextField(max_length=900, blank=False)
	timestamp 	= models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.name


class information(models.Model):
	"""docstring for information"""
	location 	= models.CharField(max_length=80, blank=False)
	email 		= models.EmailField(max_length=30, blank=False)
	email2 		= models.EmailField(max_length=30, blank=False)
	call 		= models.CharField(max_length=15, blank=False)
	call2 		= models.CharField(max_length=15, blank=False)

	def __str__(self):
		return self.location



class about(models.Model):
	title 		= models.CharField(max_length=80, blank=False)
	sub_title 	= models.TextField(max_length=150, blank=False)
	description = models.TextField(max_length=1000, blank=False)
	
	def __str__(self):
		return self.title
	