from django.shortcuts import render
from django.views import View
from loguru import logger

from .blog_services.view_services import get_posts_for_page


class BlogPageView(View):
    """Отображает страницу со всеми постами, поделенными на под-страницы пагинацией."""

    @logger.catch
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'blog_app/blog_page.html',
            context={
                'posts_for_page': get_posts_for_page(request.GET.get('page'))
            },
        )


@logger.catch
def blog_post_page(request):
    """Отображает страницу создания поста."""

    return render(request, 'blog_app/blog_post_page.html')
