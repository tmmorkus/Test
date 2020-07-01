from django.db import models

class Entity(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,blank=True)
    ico = models.CharField(max_length=8)

