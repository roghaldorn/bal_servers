from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, CharField, NumberInput, FileInput
from django.contrib.auth import get_user_model
from .models import User

FORM_CONTROL = {'class': 'form-control'}


class CustomUserCreationForm(UserCreationForm):
    password1 = CharField(label='password', widget=PasswordInput(attrs={**FORM_CONTROL, 'placeholder': 'Пароль*'}))
    password2 = CharField(label='password',
                          widget=PasswordInput(attrs={**FORM_CONTROL, 'placeholder': 'Пароль еще раз*'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'age', 'password1', 'password2', 'avatar', 'first_name', 'last_name']

        widgets = {
            'username': TextInput(attrs={
                **FORM_CONTROL,
                'placeholder': 'Имя пользователя*'
            }),
            'email': EmailInput(attrs={
                **FORM_CONTROL,
                'placeholder': 'E-Mail'
            }),
            'age': NumberInput(attrs={
                **FORM_CONTROL,
                'placeholder': 'Возраст'
            }),
            'avatar': FileInput(attrs={
                **FORM_CONTROL,
                'placeholder': 'Аватар'
            }),
            'first_name': TextInput(attrs={
                **FORM_CONTROL,
                'placeholder': 'Имя'
            }),
            'last_name': TextInput(attrs={
                **FORM_CONTROL,
                'placeholder': 'Фамилия'
            }),
        }


class CustomUserAuthenticationForm(AuthenticationForm):
    username = CharField(widget=TextInput(attrs={
        **FORM_CONTROL,
        'placeholder': 'Имя пользователя'
    }))
    password = CharField(widget=PasswordInput(attrs={
        **FORM_CONTROL,
        'placeholder': 'Пароль'
    }))


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'age', 'avatar', 'first_name', 'last_name']
        widgets = {
            'username': TextInput(attrs={
                **FORM_CONTROL,
                'placeholder': 'Имя пользователя'
            }),
            'email': EmailInput(attrs={
                **FORM_CONTROL,
                'placeholder': 'E-Mail'
            }),
            'age': NumberInput(attrs={
                **FORM_CONTROL,
                'placeholder': 'Возраст'
            }),
            'avatar': FileInput(attrs={
                **FORM_CONTROL,
                'placeholder': 'Аватар'
            }),
            'first_name': TextInput(attrs={
                **FORM_CONTROL,
                'placeholder': 'Имя'
            }),
            'last_name': TextInput(attrs={
                **FORM_CONTROL,
                'placeholder': 'Фамилия'
            }),
        }