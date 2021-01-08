from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Sentense(models.Model):
    content = models.CharField(max_length=50)