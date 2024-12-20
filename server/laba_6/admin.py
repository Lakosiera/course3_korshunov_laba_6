from django.contrib import admin
from .models import Customer, Deposit, Loan

# класс обвертка над моделью для работы в админке
class CustomerAdmin(admin.ModelAdmin):
    # отображаем поля обьекта в админке
    list_display = ('id', 'first_name', 'email', 'address')

# класс обвертка над моделью для работы в админке
class DepositAdmin(admin.ModelAdmin):
    # отображаем поля обьекта в админке
    list_display = ('id', 'customer', 'amount')

# класс обвертка над моделью для работы в админке
class LoanAdmin(admin.ModelAdmin):
    # отображаем поля обьекта в админке
    list_display = ('id', 'customer', 'amount', 'purpose', 'submitted_on', 'disbursement_on')


# регистрируем классы моделей бля работы с ними в админке
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(Loan, LoanAdmin)
