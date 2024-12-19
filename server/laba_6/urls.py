from django.urls import path

from . import views

# пути для модуля 'laba_5'
urlpatterns = [
    # корневой путь (т.е. "/" или "http://localhost:8006/")
    path(
        route="",  # путь
        view=views.index,  # вьюшка из файла 'views.py'
        name="index",  # условное имя пути
    ),
]
