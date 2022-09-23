from django.shortcuts import render


def authorization_page(request):
    return render(request, 'authorization_app/authorization_page.html')
