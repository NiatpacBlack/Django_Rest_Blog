from django.shortcuts import render


def home_page(request):
    return render(request, 'main_app/home_page.html')
