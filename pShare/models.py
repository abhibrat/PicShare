from django.db import models

class Image(models.Model):
	title = models.CharField(max_length=200)
	about = models.TextField()
	img = models.ImageField(upload_to= 'assets')

