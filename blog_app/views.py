from django.shortcuts import render
from django.views import View
from loguru import logger

from .blog_services.models_services import get_post_or_404, get_five_last_posts_in_posts_table
from .blog_services.view_services import get_posts_for_page


class BlogPageView(View):
    """Отображает страницу со всеми постами, поделенными на под-страницы пагинацией."""

    @logger.catch
    def get(self, request):
        return render(
            request,
            'blog_app/blog_page.html',
            context={
                'posts_for_page': get_posts_for_page(
                    page_number=request.GET.get('page'),
                    quantity_posts_for_page=6,
                )
            },
        )


class PostPageView(View):
    """Отображает страницу с полной информацией конкретного поста."""

    @logger.catch
    def get(self, request, url):
        return render(
            request,
            'blog_app/post_page.html',
            context={
                'post': get_post_or_404(url=url),
                'last_posts': get_five_last_posts_in_posts_table(),
            },
        )
