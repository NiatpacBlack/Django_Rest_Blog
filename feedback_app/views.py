from django.shortcuts import render


def contacts_page(request):
    return render(request, 'feedback_app/contacts_page.html')


def thanks_page(request):
    return render(request, 'feedback_app/thanks_page.html')
