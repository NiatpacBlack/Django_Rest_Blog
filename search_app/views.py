from django.shortcuts import render


def search_page(request):
    return render(request, 'search_app/search_page.html')
