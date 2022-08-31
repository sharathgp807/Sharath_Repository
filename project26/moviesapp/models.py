from django.db import models

# Create your models here.

class MovieTable(models.Model):
	moviename = models.CharField(max_length = 20)
	hero = models.CharField(max_length = 20)
	heroine = models.CharField(max_length = 20)