from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    password = models.CharField(max_length=50)

    #signature = models.choices()
    #avatar = models.ImageField()