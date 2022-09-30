from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class PostModel(models.Model):
    """Таблица описывающая поля отдельного поста из блога."""

    heading = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    url = models.SlugField()
    description = RichTextUploadingField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    created_data = models.DateField(default=timezone.now)
    tag = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts"
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
