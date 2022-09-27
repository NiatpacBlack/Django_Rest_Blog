from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class FeedBackForm(forms.Form):
    """Форма отправки обратной связи администратору."""

    name = forms.CharField(
        label='',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control my-3",
            'placeholder': "Ваше имя",
            'id': "inputName",
        }),
    )
    email = forms.CharField(
        label='',
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': "form-control my-3",
            'placeholder': "Ваша почта",
            'id': "inputEmail",
        }),
    )
    subject = forms.CharField(
        label='',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control my-3",
            'placeholder': "Тема",
            'id': "inputSubject",
        }),
    )
    message = forms.CharField(
        label='',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control my-3",
            'placeholder': "Тема",
            'id': "inputMessage",
        }),
    )

    def __init__(self, *args, **kwargs):
        """При создании объекта класса - FormHelper создаст html шаблон форм."""

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'email',
            'subject',
            'message',
            Submit('submit', 'Отправить', css_class='btn btn-primary'),
        )
