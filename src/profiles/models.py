# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from groups.models import Game


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    os = models.CharField(max_length=80, blank=True)
    cpu = models.CharField(max_length=80, blank=True)
    gpu = models.CharField(max_length=80, blank=True)
    ram = models.CharField(max_length=80, blank=True)
    monitor = models.CharField(max_length=80, blank=True)
    cpu = models.CharField(max_length=80, blank=True)
    ssd = models.CharField(max_length=80, blank=True)
    hdd = models.CharField(max_length=80, blank=True)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
