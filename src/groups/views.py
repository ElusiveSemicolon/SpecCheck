# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages

from . import models
from groups.models import Group,GroupMember


class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = Group


class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group


class JoinGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    #this is to get a message of whether you are a group member or not
    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

        # going to try and get group member object and create it
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,'Already a member!')
        else:
            messages.success(self.request,'You are now a member!')

        return super(JoinGroup,self).get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):

        try:
            membership = models.GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug')).get()

        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry you are not in this group!')
        else:
            membership.delete()
            messages.success(self.request,'You have left the group!')
        return super(LeaveGroup,self).get(request,*args,**kwargs)
