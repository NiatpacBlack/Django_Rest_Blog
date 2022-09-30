from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.forms import ModelForm

from blog_app.models import PostModel


class CreatePostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """При создании объекта класса - FormHelper создаст html шаблон форм."""

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'heading',
            'title',
            'image',
            'url',
            'description',
            'content',
            'author',
            'created_data',
            'tag',
            Submit('submit', 'Регистрация', css_class='btn my-3 btn-lg btn-primary btn-block'),
        )

    def save_new_post(self):
        """Внести данные нового пользователя в таблицу User. И аутентифицировать его."""

        new_post = PostModel.objects.create(
            heading=self.cleaned_data['heading'],
            title=self.cleaned_data['title'],
            image=self.cleaned_data['image'],
            url=self.cleaned_data['url'],
            description=self.cleaned_data['description'],
            content=self.cleaned_data['content'],
            author=self.cleaned_data['author'],
            created_data=self.cleaned_data['created_data'],
            tag=self.cleaned_data['tag'],
        )
        new_post.save()