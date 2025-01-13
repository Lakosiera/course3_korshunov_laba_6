from rest_framework import serializers
from .models import Customer, Deposit, Loan


# сериализатор модели
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        # модель
        model = Deposit
        # поля для сериализации
        fields = ["id", "amount"]
        # поле только для чтения
        read_only_fields = ["id"]


# сериализатор модели
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        # модель
        model = Loan
        # поля для сериализации
        fields = ["id", "amount", "purpose", "submitted_on", "disbursement_on"]
        # поле только для чтения
        read_only_fields = ["id"]


# сериализатор модели
class CustomerSerializer(serializers.ModelSerializer):
    # отображаем данные из связанной таблицы как объекты
    # присоединяем в поле вклады все связанные данные
    deposits = DepositSerializer(
        many=True,  # как массив
    )
    # присоединяем в поле займы все связанные данные
    loans = LoanSerializer(
        many=True,  # как массив
    )

    class Meta:
        # модель
        model = Customer
        # поля для сериализации
        fields = ["id", "first_name", "email", "address", "deposits", "loans"]
        # поле только для чтения
        read_only_fields = ["id"]

    # переопределяем метод создания нового экземпляра данных
    # для того чтобы можно было создавать сразу вклады и займы
    def create(self, validated_data):
        # извлекаем данные нужные для создания вкладов
        deposits_data = validated_data.pop("deposits")
        # извлекаем данные нужные для создания займов
        loans_data = validated_data.pop("loans")

        # создаем новый экземпляр клиента
        customer = Customer.objects.create(**validated_data)

        # перебираем данные вкладов
        for deposit in deposits_data:
            # создаем экземпляр вклада указав какому клиенту он принадлежит
            Deposit.objects.create(customer=customer, **deposit)

        # перебираем данные займов
        for loan in loans_data:
            # создаем экземпляр займа указав какому клиенту он принадлежит
            Loan.objects.create(customer=customer, **loan)

        # возвращаем созданного клиента
        return customer
