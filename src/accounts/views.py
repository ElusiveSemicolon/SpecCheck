
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from . import forms
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm #connect to method
    success_url = reverse_lazy('login') #send them back to the login page once they finished sign-up
    template_name = 'accounts/signup.html'

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

