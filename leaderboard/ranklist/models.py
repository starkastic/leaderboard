from django.db import models

class Team(models.Model):
    score = models.IntegerField(default=0)
    player_1 = models.CharField(max_length=250, default=None)
    player_2 = models.CharField(max_length=250, default=None)