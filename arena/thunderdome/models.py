from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100, default="")

class Game(models.Model):
    clients = models.ManyToManyField(Client, through='GameData',
                                     related_name='games_played')

    winner = models.ForeignKey(Client, null=True, blank=True,
                               related_name='games_won')
    loser = models.ForeignKey(Client, null=True, blank=True,
                              related_name='games_lost')


class GameData(models.Model):
    game = models.ForeignKey(Game)
    client = models.ForeignKey(Client)
    won = models.NullBooleanField()
