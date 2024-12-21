from rest_framework import serializers
from .models import Customer, Deposit, Loan



class CustomerSerializer(serializers.ModelSerializer):
    # deposits = serializers.PrimaryKeyRelatedField(many=True, queryset=Deposit.objects.all())
    # loans = serializers.PrimaryKeyRelatedField(many=True, queryset=Loan.objects.all())
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'email', 'address', 'deposits', 'loans']
        read_only_fields = ['id']


class DepositSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.customer')
    class Meta:
        model = Deposit
        fields = '__all__'
        read_only_fields = ['id']


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
        read_only_fields = ['id']

