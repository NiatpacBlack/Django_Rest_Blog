from django.shortcuts import render
from django.views import View
from .blog_services.models_services import get_all_posts_from_blog


class BlogPageView(View):
    def get(self, request, *args, **kwargs):
        all_posts = get_all_posts_from_blog()
        # for post in all_posts:
        #     print(post.image)
        return render(request, 'blog_app/blog_page.html', context={'all_posts': all_posts})


# def blog_page(request):
#     return render(request, 'blog_app/blog_page.html')


def blog_post_page(request):
    return render(request, 'blog_app/blog_post_page.html')
