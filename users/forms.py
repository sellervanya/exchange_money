# users/forms.py
'''
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):

    iq = forms.IntegerField(label='iq')

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'iq')


class CustomUserChangeForm(UserChangeForm):

    iq = forms.IntegerField(label='iq')

    class Meta:
        model = User
        fields = ('username', 'email', 'iq', )
'''
