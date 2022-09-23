from django.shortcuts import render


def registration_page(request):
    return render(request, 'registration_app/registration_page.html')
