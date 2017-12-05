# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
# Register your models here.

class ChoiceAdmin(admin.ModelAdmin):
    autocomplete_fields = ['game']

class GroupMemberInline(admin.TabularInline):
    model=models.GroupMember

admin.site.register(models.Group)
