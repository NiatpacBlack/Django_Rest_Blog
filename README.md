# Django_Blog

Полноценный блог, в котором можно добавлять статьи и читать статьи других людей.

Сайт поддерживает регистрацию и авторизацию пользователей, имеет форму обратной связи и поиска статей по тегам и словам.
На главной странице можно разместить рекламу различных статей, я в данном случае разместил ссылки на другие свои проекты.

## Запуск проекта
   * Версия python 3.10.7
   * Устанавливаем зависимости из requirements.txt: `pip install -r requirements.txt` Для Unix-систем вместо `pip` потребуется `pip3`.
   * Вводим команду: `python manage.py runserver`
   * (Необязательно) В файле settings.py указать значения в переменные. Нужно для функционирования отправки обратной связи на почту.:
      - `EMAIL_HOST_USER` (ваш email куда будут приходить письма с обратной связью)
      - `EMAIL_HOST_PASSWORD` (пароль для связи с приложением. который можно посмотреть на вашей почте)
## Превью сайта
![Peek 2022-10-01 20-50](https://user-images.githubusercontent.com/84034483/193422746-15029237-e39b-4c8a-9ece-e67e48e1f14c.gif)
