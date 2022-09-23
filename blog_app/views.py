from django.shortcuts import render


def blog_page(request):
    return render(request, 'blog_app/blog_page.html')


def blog_post_page(request):
    return render(request, 'blog_app/blog_post_page.html')
