from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from loguru import logger

from authorization_app.authorization_services.services import authenticate_user
from registration_app.forms import RegistrationForm


class RegistrationView(View):
    """Представление страницы регистрации пользователей. Я знаю, что есть стандартное в django. Это для учебы."""

    @logger.catch
    def get(self, request):
        """Отображает шаблон страницы регистрации с формой."""

        return render(
            request,
            'registration_app/registration_page.html',
            context={'form': RegistrationForm()},
        )

    @logger.catch
    def post(self, request):
        """При корректно заполненной форме в таблице User будет создан новый пользователь и авторизован на сайте."""

        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save_new_user()
            new_user = authenticate_user(form)
            if new_user is not None:
                login(request, new_user)
                return HttpResponseRedirect('/')
        return render(
            request,
            'registration_app/registration_page.html',
            context={'form': form},
        )
