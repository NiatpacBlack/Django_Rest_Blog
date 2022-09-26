from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from loguru import logger

from registration_app.forms import RegistrationForm


class RegistrationView(View):
    """Представление страницы регистрации пользователей."""

    @logger.catch
    def get(self, request):
        return render(
            request,
            'registration_app/registration_page.html',
            context={'form': RegistrationForm()},
        )

    @logger.catch
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save_new_user()
            if new_user is not None:
                login(request, new_user)
                return HttpResponseRedirect('/')
        return render(
            request,
            'registration_app/registration_page.html',
            context={'form': form},
        )
