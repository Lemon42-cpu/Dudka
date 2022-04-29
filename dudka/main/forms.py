from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput


class RegisterUserForm(UserCreationForm):
    # username = forms,
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Логин'
            }),
            'password1': TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Пароль'
            }),
            'password2': TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Пароль'
            })
        }