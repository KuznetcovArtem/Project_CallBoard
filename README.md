# Доска объявлений

## Учебный проект на онлайн-курсе Fullstack разработчик на Python

### Как установить:
Python3 должен быть уже установлен.<br>

Для установки зависимостей
```commandline
pip install -r requirements.txt
```

Для запуска, в корне проекта необходимо создать файл .env со следующими настройками:
````python
# Development settings

# Yandex.ru
EMAIL_HOST_YANDEX=<Сервер исходящей почты>
EMAIL_PORT_YANDEX=<Порт исходящей почты>
EMAIL_HOST_USER_YANDEX=<Имя пользователя>
EMAIL_HOST_PASSWORD_YANDEX=<Пароль пользователя>
DEFAULT_FROM_EMAIL_YANDEX=<Полный адрес пользователя исходящей почты>
````

## Основные страницы:<br>

### Запуск сервера на локальной машине
```commandline
python manage.py runserver
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе "Fullstack разработчик на Python" [Skillfactory.ru](https://skillfactory.ru)
