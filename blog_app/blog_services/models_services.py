from blog_app.models import PostModel


def get_all_posts_from_blog():
    """Возвращает QuerySet всех постов в таблице PostModel."""

    return PostModel.objects.all()


