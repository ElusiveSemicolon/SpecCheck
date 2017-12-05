
from __future__ import unicode_literals

from django.db import models
from django.contrib import auth
from groups.models import Game
from posts.models import Post





# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __unicode__(self):
        return "@{}".format(self.username)
