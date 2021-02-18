from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User, GEN_CHOICES


class SignUpForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=64, label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )

    last_name = forms.CharField(
        max_length=64, label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )

    gender = forms.ChoiceField(
        choices=GEN_CHOICES, label='Пол',
        widget=forms.Select(attrs={'class': 'form-control'})
        )

    document_id = forms.CharField(
        max_length=64, label='Номер документа',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )

    email = forms.EmailField(
        max_length=64, label='Адрес электронной почты',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
        )

    username = forms.CharField(
        max_length=64, label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )

    password1 = forms.CharField(
        max_length=64, label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )

    password2 = forms.CharField(
        max_length=64, label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )

    phone_number = forms.CharField(
        max_length=12, label='Номер телефона',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'gender',
            'document_id', 'email', 'username',
            'password1', 'password2', 'phone_number', )


class SignInForm(AuthenticationForm):
    username = forms.CharField(
        max_length=64, label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )

    password = forms.CharField(
        max_length=64, label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )


class UserForm(forms.ModelForm):

    password = forms.CharField(
        max_length=64, label='Текущий пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
    forms.EmailInput

    class Meta:
        model = User
        fields = ('email', )
        widgets = {
            'email': forms.EmailInput(
                attrs={'class': 'form-control'})
            }
