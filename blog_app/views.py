from django.shortcuts import render
from django.views import View
from loguru import logger

from .blog_services.models_services import get_post_or_404
from .blog_services.view_services import get_posts_for_page


class BlogPageView(View):
    """Отображает страницу со всеми постами, поделенными на под-страницы пагинацией."""

    @logger.catch
    def get(self, request):
        return render(
            request,
            'blog_app/blog_page.html',
            context={
                'posts_for_page': get_posts_for_page(request.GET.get('page'))
            },
        )


class PostPageView(View):
    """Отображает страницу создания поста."""

    @logger.catch
    def get(self, request, url):
        return render(
            request,
            'blog_app/post_page.html',
            context={
                'post': get_post_or_404(url=url)
            },
        )
