# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

#shows list of posts related to group/user
class PostList(SelectRelatedMixin,generic.ListView):
    model = models.Post
    select_related = ('user','group')


#shows a specific post
class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    #try to set the user to user's objects (posts)
    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context=super(UserPosts,self).get_context_data(**kwargs)
        context['post_user'] = self.post_user
        names = ['Operating System', 'Graphics Card', 'Monitor', 'CPU', 'RAM', 'SSD', 'HDD']
        flds = ['os', 'gpu', 'monitor', 'cpu', 'ram', 'ssd', 'hdd']
        vals = [getattr(self.post_user.profile, x) for x in flds]
        context['profile'] = zip(names,flds,vals)
        context['is_user'] = self.post_user.id == self.request.user.id
        return context


class PostDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    select_related = ('user','group')

    def get_queryset(self):
        queryset=super(PostDetail,self).get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    form_class = forms.PostForm
    #filter(members__username__contains=User.username)
    model = models.Post

    def get_form_kwargs(self):
        kwargs = super(CreatePost, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(CreatePost,self).form_valid(form)


class DeletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):

    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')


    def get_queryset(self):
        queryset = super(DeletePost,self).get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted')
        return super(DeletePost, self).delete(*args,**kwargs)
