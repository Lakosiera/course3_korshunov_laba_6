from django.urls import path

from . import views

# пути для модуля 'laba_5'
urlpatterns = [
    # корневой путь (т.е. "/" или "http://localhost:8004/")
    path(
        route="",  # путь
        view=views.hello_world,  # вьюшка из файла 'views.py'
        name="index",  # условное имя пути
    ),
]
