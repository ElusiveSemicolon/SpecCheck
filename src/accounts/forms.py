from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
User = get_user_model()


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2', )
        #'os', 'cpu', 'gpu', 'ram', 'monitor', 'cpu', 'ssd', 'hdd'
        model = User

# we are changing the label to display a diff text to the user as they are creating new account
    def __init__(self,*args,**kwargs):
        super(UserCreateForm, self).__init__(*args,**kwargs)
        self.fields['username'].label= 'Display Name'
        self.fields['email'].label= "Email Address"
        # self.fields['os'].label = 'Operating System'
        # self.fields['gpu'].label = 'Graphics Card'
        # self.fields['cpu'].label = 'Central Processing Unit'
        # self.fields['ram'].label = 'RAM'
        # self.fields['ssd'].label = 'Solid State Drive'
        # self.fields['hdd'].label = 'Hard Disk Drive'
