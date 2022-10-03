from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from django.forms import ModelForm, Textarea

from blog_app.models import PostModel, CommentModel


class CreatePostForm(ModelForm):
    """
    Форма создания нового поста в блоге. Основана на модели PostModel.

    Для создания формы используется crispy-forms, шаблон полей создается в __init__.
    """

    class Meta:
        model = PostModel
        fields = [
            "heading",
            "title",
            "image",
            "description",
            "content",
            "tag",
        ]

    def __init__(self, *args, **kwargs):
        """При создании объекта класса - FormHelper создаст html шаблон форм."""

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "heading",
            "title",
            "image",
            "description",
            "content",
            "tag",
            Submit(
                "submit",
                "Опубликовать",
                css_class="btn my-3 btn-lg btn-primary btn-block",
            ),
        )


class CommentForm(ModelForm):
    """
    Форма создания нового комментария. Основана на модели CommentModel.

    Для создания формы используется crispy-forms, шаблон полей создается в __init__.
    """

    class Meta:
        model = CommentModel
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }

    def __init__(self, *args, **kwargs):
        """При создании объекта класса - FormHelper создаст html шаблон форм."""

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'text',
            HTML('<input type="submit" value="Отправить" class="btn my-3 btn-primary btn-block">'),
        )
