from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.forms import ModelForm, Textarea

from blog_app.models import PostModel, CommentModel


class CreatePostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """При создании объекта класса - FormHelper создаст html шаблон форм."""

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "heading",
            "title",
            "image",
            "url",
            "description",
            "content",
            "author",
            "created_data",
            "tag",
            Submit(
                "submit",
                "Опубликовать",
                css_class="btn my-3 btn-lg btn-primary btn-block",
            ),
        )


class CommentForm(ModelForm):
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
            Submit(
                "submit",
                "Опубликовать",
                css_class="btn my-3 btn-primary btn-block",
            ),
        )
