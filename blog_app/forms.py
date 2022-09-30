from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.forms import ModelForm

from blog_app.models import PostModel


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
