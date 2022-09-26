from django.core.paginator import Paginator

from .models_services import get_all_posts_from_blog


def get_posts_for_page(page_number: str):
    """Возвращает QuerySet 6 постов из таблицы PostModel в зависимости от номера выбранной страницы page_number."""

    all_posts = get_all_posts_from_blog()
    paginator = Paginator(all_posts, 6)
    posts_for_page = paginator.get_page(page_number)
    return posts_for_page
