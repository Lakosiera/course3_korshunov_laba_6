from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Customer, Deposit, Loan


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Customer
        fields = ['deposits', 'loans', 'id', 'first_name', 'email', 'address']
        read_only_fields = ['id']


class DepositSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'
        read_only_fields = ['id']


class LoanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
        read_only_fields = ['id']

