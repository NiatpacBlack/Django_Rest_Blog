from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from authorization_app.authorization_services.services import authenticate_user


class RegistrationForm(forms.Form):
    """Форма регистрации нового пользователя."""

    username = forms.CharField(
        label='',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control my-3",
            'placeholder': "Введите имя пользователя",
            'id': "inputUsername",
        }),
    )
    password = forms.CharField(
        label='',
        max_length=255,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control my-3",
            'placeholder': "Введите пароль",
            'id': "inputPassword",
        }),
    )
    repeat_password = forms.CharField(
        label='',
        max_length=255,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control my-3",
            'placeholder': "Повторите пароль",
            'id': "ReInputPassword",
        }),
    )

    def __init__(self, *args, **kwargs):
        """При создании объекта класса FormHelper создаст html шаблон форм."""

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            'repeat_password',
            Submit('submit', 'Регистрация', css_class='btn my-3 btn-lg btn-primary btn-block')
        )

    def clean(self):
        """Вернет ошибку если пароль не совпадает с подтверждением пароля."""

        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        if password != confirm_password:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )

    def save_new_user(self):
        """Внести данные нового пользователя в таблицу User. И аутентифицировать его."""

        new_user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        new_user.save()
        return authenticate_user(self)
