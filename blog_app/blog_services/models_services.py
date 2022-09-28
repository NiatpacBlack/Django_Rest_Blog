from django.db.models import Q
from django.shortcuts import get_object_or_404

from blog_app.models import PostModel


def get_post_or_404(url: str):
    """Возвращает определенный пост из таблицы PostModel по url, или 404."""

    return get_object_or_404(PostModel, url=url)


def get_all_posts_from_blog():
    """Возвращает QuerySet всех постов в таблице PostModel. В обратном порядке."""

    return PostModel.objects.all()[::-1]


def find_query_in_posts_table(query: str):
    """
    Возвращает QuerySet из тех постов, в который найден запрос query. Выводит начиная с самого нового.

    Поиск происходит в заголовках и основном контенте поста.
    """

    return PostModel.objects.filter(
        Q(heading__icontains=query) | Q(content__icontains=query)
    )[::-1]
