from django.http import Http404
from rest_framework import viewsets, permissions, views, status, renderers
from rest_framework.response import Response
from .serializers import CustomerSerializer, DepositSerializer, LoanSerializer
from .models import Customer, Deposit, Loan

# REST CRUD

# клиенты

class CustomerList(views.APIView):
    # разрешения
    permission_classes = [permissions.IsAuthenticated]
    # рендер вьюшки
    renderer_classes = [
        renderers.JSONRenderer,  # рендерим как json
    ]

    # Читаем все объекты
    def get(self, request):
        # получаем все объекты из базы
        objects = Customer.objects.all()
        # вериализуем как список
        serializer = CustomerSerializer(
            objects,  # объектыдля сериализации
            many=True,  # как список
        )
        # ответ
        return Response(serializer.data)

    # Создае новый обьект
    def post(self, request):
        # сериализуем
        serializer = CustomerSerializer(
            data=request.data,  # данные из тела запроса
        )
        # если данные верны
        if serializer.is_valid():
            # сохраняем в базу данных
            serializer.save()
            # ответ
            return Response(
                serializer.data,  # данные ответ
                status=status.HTTP_201_CREATED,  # статус ответа 201 - создано
            )
        # в случае если данные не верны
        return Response(
            serializer.errors,  # вотзвращаем ошибки
            status=status.HTTP_400_BAD_REQUEST,  # статус ответа 400 - плохой запрос
        )


class CustomerDetail(views.APIView):
    # разрешения
    permission_classes = [permissions.IsAuthenticated]
    # рендер вьюшки
    renderer_classes = [
        renderers.JSONRenderer,  # рендерим как json
    ]

    # утилитарный метод получения объекта по id
    def _get_object(self, customer_id):
        try:
            # получаем объект по id
            return Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            # ловим исключение что файл не существует
            # возвращаем ответе 404 - не найдено
            raise Http404

    # метод GET получение объекта по id
    def get(self, request, customer_id):
        # получаем объект
        object = self._get_object(customer_id)
        # сериализуем
        serializer = CustomerSerializer(object)
        # ответ
        return Response(serializer.data)

    # метод PATCH обновить объект по id новыми данными
    def patch(self, request, customer_id):
        # получаем объект
        object = self._get_object(customer_id)
        # сериализуем объект из тела запроса
        serializer = CustomerSerializer(
            object,  # объект из БД
            data=request.data,  # тело запроса
            partial=True,  # частичное обновление (все поля не обязательны)
        )
        # если данные верны
        if serializer.is_valid():
            # сохраняем в базу данных
            serializer.save()
            # ответ
            return Response(serializer.data)
        # в случае если данные не верны
        return Response(
            serializer.errors,  # вотзвращаем ошибки
            status=status.HTTP_400_BAD_REQUEST,  # статус ответа 400 - плохой запрос
        )

    # метод DELET удалит объект по id
    def delete(self, request, customer_id):
        # получаем объект
        object = self._get_object(customer_id)
        # удалить
        object.delete()
        # ответ
        return Response(
            status=status.HTTP_204_NO_CONTENT,  # статус ответа 204 - нет данных для отображения
        )

# вклады

class DepositList(views.APIView):
    # разрешения
    permission_classes = [permissions.IsAuthenticated]
    # рендер вьюшки
    renderer_classes = [
        renderers.JSONRenderer,  # рендерим как json
    ]

    # утилитарный метод получения объекта по id
    def _get_customer(self, customer_id):
        try:
            # получаем объект по id
            return Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            # ловим исключение что файл не существует
            # возвращаем ответе 404 - не найдено
            raise Http404

    # Читаем все объекты
    def get(self, request, customer_id):
        _ = self._get_customer(customer_id)
        # получаем все объекты из базы для которых верно условеие
        objects = Deposit.objects.filter(customer=customer_id)
        # вериализуем как список
        serializer = DepositSerializer(
            objects,  # объектыдля сериализации
            many=True,  # как список
        )
        # ответ
        return Response(serializer.data)

    # Создае новый обьект
    def post(self, request, customer_id):
        # получаем клиента
        customer = self._get_customer(customer_id)
        # сериализуем
        serializer = DepositSerializer(
            data=request.data,  # данные из тела запроса
        )
        # если данные верны
        if serializer.is_valid():
            # сохраняем в базу данных
            serializer.save(
                customer=customer, # устанавливаем значение клиента принудительно
            )
            # ответ
            return Response(
                serializer.data,  # данные ответ
                status=status.HTTP_201_CREATED,  # статус ответа 201 - создано
            )
        # в случае если данные не верны
        return Response(
            serializer.errors,  # вотзвращаем ошибки
            status=status.HTTP_400_BAD_REQUEST,  # статус ответа 400 - плохой запрос
        )


class DepositDetail(views.APIView):
    # разрешения
    permission_classes = [permissions.IsAuthenticated]
    # рендер вьюшки
    renderer_classes = [
        renderers.JSONRenderer,  # рендерим как json
    ]

    # утилитарный метод получения объекта по id
    def _get_customer(self, customer_id):
        try:
            # получаем объект по id
            return Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            # ловим исключение что файл не существует
            # возвращаем ответе 404 - не найдено
            raise Http404

    # утилитарный метод получения объекта по id
    def _get_object(self, customer_id, id):
        try:
            # получаем объект по id
            return Deposit.objects.get(pk=id, customer=customer_id)
        except Deposit.DoesNotExist:
            # ловим исключение что файл не существует
            # возвращаем ответе 404 - не найдено
            raise Http404

    # метод GET получение объекта по id
    def get(self, request, customer_id, id):
        # получаем объект
        object = self._get_object(customer_id, id)
        # сериализуем
        serializer = DepositSerializer(object)
        # ответ
        return Response(serializer.data)

    # метод PATCH обновить объект по id новыми данными
    def patch(self, request, customer_id, id):
        # получаем объект
        object = self._get_object(customer_id, id)
        # сериализуем объект из тела запроса
        serializer = DepositSerializer(
            object,  # объект из БД
            data=request.data,  # тело запроса
            partial=True,  # частичное обновление (все поля не обязательны)
        )
        # если данные верны
        if serializer.is_valid():
            # сохраняем в базу данных
            serializer.save()
            # ответ
            return Response(serializer.data)
        # в случае если данные не верны
        return Response(
            serializer.errors,  # вотзвращаем ошибки
            status=status.HTTP_400_BAD_REQUEST,  # статус ответа 400 - плохой запрос
        )

    # метод DELET удалит объект по id
    def delete(self, request, customer_id, id):
        # получаем объект
        object = self._get_object(customer_id, id)
        # удалить
        object.delete()
        # ответ
        return Response(
            status=status.HTTP_204_NO_CONTENT,  # статус ответа 204 - нет данных для отображения
        )

# займы

class LoanList(views.APIView):
    # разрешения
    permission_classes = [permissions.IsAuthenticated]
    # рендер вьюшки
    renderer_classes = [
        renderers.JSONRenderer,  # рендерим как json
    ]

    # утилитарный метод получения объекта по id
    def _get_customer(self, customer_id):
        try:
            # получаем объект по id
            return Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            # ловим исключение что файл не существует
            # возвращаем ответе 404 - не найдено
            raise Http404

    # Читаем все объекты
    def get(self, request, customer_id):
        _ = self._get_customer(customer_id)
        # получаем все объекты из базы для которых верно условеие
        objects = Loan.objects.filter(customer=customer_id)
        # вериализуем как список
        serializer = LoanSerializer(
            objects,  # объектыдля сериализации
            many=True,  # как список
        )
        # ответ
        return Response(serializer.data)

    # Создае новый обьект
    def post(self, request, customer_id):
        # получаем клиента
        customer = self._get_customer(customer_id)
        # сериализуем
        serializer = LoanSerializer(
            data=request.data,  # данные из тела запроса
        )
        # если данные верны
        if serializer.is_valid():
            # сохраняем в базу данных
            serializer.save(
                customer=customer, # устанавливаем значение клиента принудительно
            )
            # ответ
            return Response(
                serializer.data,  # данные ответ
                status=status.HTTP_201_CREATED,  # статус ответа 201 - создано
            )
        # в случае если данные не верны
        return Response(
            serializer.errors,  # вотзвращаем ошибки
            status=status.HTTP_400_BAD_REQUEST,  # статус ответа 400 - плохой запрос
        )

class LoanDetail(views.APIView):
    # разрешения
    permission_classes = [permissions.IsAuthenticated]
    # рендер вьюшки
    renderer_classes = [
        renderers.JSONRenderer,  # рендерим как json
    ]

    # утилитарный метод получения объекта по id
    def _get_customer(self, customer_id):
        try:
            # получаем объект по id
            return Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            # ловим исключение что файл не существует
            # возвращаем ответе 404 - не найдено
            raise Http404

    # утилитарный метод получения объекта по id
    def _get_object(self, customer_id, id):
        try:
            # получаем объект по id
            return Loan.objects.get(pk=id, customer=customer_id)
        except Loan.DoesNotExist:
            # ловим исключение что файл не существует
            # возвращаем ответе 404 - не найдено
            raise Http404

    # метод GET получение объекта по id
    def get(self, request, customer_id, id):
        # получаем объект
        object = self._get_object(customer_id, id)
        # сериализуем
        serializer = LoanSerializer(object)
        # ответ
        return Response(serializer.data)

    # метод PATCH обновить объект по id новыми данными
    def patch(self, request, customer_id, id):
        # получаем объект
        object = self._get_object(customer_id, id)
        # сериализуем объект из тела запроса
        serializer = LoanSerializer(
            object,  # объект из БД
            data=request.data,  # тело запроса
            partial=True,  # частичное обновление (все поля не обязательны)
        )
        # если данные верны
        if serializer.is_valid():
            # сохраняем в базу данных
            serializer.save()
            # ответ
            return Response(serializer.data)
        # в случае если данные не верны
        return Response(
            serializer.errors,  # вотзвращаем ошибки
            status=status.HTTP_400_BAD_REQUEST,  # статус ответа 400 - плохой запрос
        )

    # метод DELET удалит объект по id
    def delete(self, request, customer_id, id):
        # получаем объект
        object = self._get_object(customer_id, id)
        # удалить
        object.delete()
        # ответ
        return Response(
            status=status.HTTP_204_NO_CONTENT,  # статус ответа 204 - нет данных для отображения
        )


# Django REST вьюшки для просмотра API
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepositViewSet(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    permission_classes = [permissions.IsAuthenticated]


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]