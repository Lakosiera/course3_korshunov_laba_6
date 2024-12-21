from django.db import models


# модель клиентов
class Customer(models.Model):
    first_name = models.CharField(
        verbose_name="Имя",  # название столбца в админке и ошибках
        max_length=30,  # максимальная длина текста
        help_text="Имя",
    )
    email = models.EmailField(
        verbose_name="Почта",  # название столбца в админке и ошибках
        max_length=50,  # максимальная длина текста
        help_text="Почта",
    )
    address = models.CharField(
        verbose_name="Адрес",  # название столбца в админке и ошибках
        max_length=50,  # максимальная длина текста
        help_text="Адрес",
    )

# модель вкладов
class Deposit(models.Model):
    # поле внешней зависимости
    customer = models.ForeignKey(
        to=Customer, # зависит от Клиента
        related_name='deposits', # имя что будет использовано в Клинете для отображения всех связанных вкладов
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(
        verbose_name="Сумма",  # название столбца в админке и ошибках
        help_text="Сумма",
    )


# модель займов
class Loan(models.Model):
    # поле внешней зависимости
    customer = models.ForeignKey(
        to=Customer, # зависит от Клиента
        related_name='loans', # имя что будет использовано в Клинете для отображения всех связанных займов
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(
        verbose_name="Сумма",  # название столбца в админке и ошибках
        help_text="Сумма",
    )
    purpose = models.CharField(
        verbose_name="Цель кредита",  # название столбца в админке и ошибках
        max_length=50,  # максимальная длина текста
        help_text="Цель кредита",
    )
    submitted_on = models.DateField(
        verbose_name="Представлено",  # название столбца в админке и ошибках
        help_text="Представлено",
    )
    disbursement_on = models.DateField(
        verbose_name="Погасить до",  # название столбца в админке и ошибках
        help_text="Погасить до",
    )
