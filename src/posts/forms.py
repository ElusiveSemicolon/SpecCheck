from django import forms
from .models import Post
from groups.models import Group

class PostForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = ['message', 'group']

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(PostForm, self).__init__(*args, **kwargs)
       self.fields['message'].required = True
       self.fields['group'].required = True
       self.fields['group'].queryset = Group.objects.filter(members__username__contains=user.username)