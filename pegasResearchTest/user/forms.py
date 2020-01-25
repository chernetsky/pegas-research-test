from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm as NativeUserCreationForm,
    PasswordChangeForm as NativePasswordChangeForm
)
from django.contrib.auth.forms import PasswordChangeForm


class UserCreationForm(NativeUserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PasswordChangeForm(NativePasswordChangeForm):
    ''' Just override for now. '''
    pass
