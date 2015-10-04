from django.db import models

# Create your models here.


class Game(models.Model):
    winner = models.CharField(max_length=20)
    
