from __future__ import unicode_literals

from django.db import models
from django.utils.deconstruct import deconstructible
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify #remove characters that aren't alphanumeric or etc
from django.core.urlresolvers import reverse

# Create your models here.

#this allow us to do link embedding (like in reddit)
import misaka

from django.contrib.auth import get_user_model
User = get_user_model() # call things off current user session

from select2 import fields as select2_fields

from django import template
register = template.Library()

@deconstructible
class Game(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    name = models.TextField(blank=True)
    year = models.TextField(blank=True)
    url = models.URLField(blank=True)
    cover_url = models.URLField(blank=True)
    summary = models.TextField(blank=True)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.year)

@python_2_unicode_compatible
class Group(models.Model):
    game = models.OneToOneField(Game, related_name="groups", null=True, blank=True)
    slug = models.SlugField(allow_unicode=True,unique=True) #dont want url group slug and name to overlap
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User,through='GroupMember')
    name = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.name = self.game.name
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super(Group, self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['game']

#connects to a group that a group member belongs to and
#user that connects to the individual member
class GroupMember(models.Model):

    group = models.ForeignKey(Group,related_name='memberships')
    user = models.ForeignKey(User,related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group','user')
