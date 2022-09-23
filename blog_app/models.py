from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PostModel(models.Model):
    """Таблица описывающая поля отдельного поста из блога"""

    # Заголовок
    heading = models.CharField(max_length=100)
    # Название поста
    title = models.CharField(max_length=100)
    # Картинка поста
    image = models.ImageField()
    # Ссылка на пост
    url = models.SlugField()
    # Описание поста
    description = models.TextField()
    # Контент поста
    content = models.TextField()
    # Автор поста, из таблицы пользователей
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Время создания поста, по умолчанию текущее время
    created_at = models.DateField(default=timezone.now)
    # Теги относящиеся к теме поста
    tags = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
