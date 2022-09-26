from django.shortcuts import get_object_or_404

from blog_app.models import PostModel


def get_post_or_404(url: str):
    """Возвращает определенный пост из таблицы PostModel по url, или 404."""

    return get_object_or_404(PostModel, url=url)


def get_all_posts_from_blog():
    """Возвращает QuerySet всех постов в таблице PostModel."""

    return PostModel.objects.all()
