from blog_app.models import PostModel


def get_all_posts_from_blog():
    return PostModel.objects.all()


