
from __future__ import unicode_literals

from django.db import models
from django.contrib import auth
from groups.models import Game

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    os = models.CharField(max_length=80, blank=True)
    cpu = models.CharField(max_length=80, blank=True)
    gpu = models.CharField(max_length=80, blank=True)
    ram = models.CharField(max_length=80, blank=True)
    monitor = models.CharField(max_length=80, blank=True)
    cpu = models.CharField(max_length=80, blank=True)
    ssd = models.CharField(max_length=80, blank=True)
    hdd = models.CharField(max_length=80, blank=True)
    favorite_game = models.ForeignKey(Game, related_name='users',null=True,blank=True)

    def __unicode__(self):
        return "@{}".format(self.username)
