from django.shortcuts import render
from django.http import HttpResponse

# пример простейшей вьющки
def hello_world(request):
    # простейший вывод html страницы
    return HttpResponse("Hello, world!")

# вьбшка главной страници
def index(request):
    # передаем данные контекста
    context = {
        # параметр заголовока
        "name": "Laba 6 - API Кредитный банк",

    }
    # ренедр вьюшки в html страницу
    return render(request, "index.html", context)