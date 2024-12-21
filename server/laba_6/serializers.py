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
    deposits = DepositSerializer(many=True, read_only=True)
    loans = LoanSerializer(many=True, read_only=True)

    class Meta:
        # модель
        model = Customer
        # поля для сериализации
        fields = ["id", "first_name", "email", "address", "deposits", "loans"]
        # поле только для чтения
        read_only_fields = ["id"]
