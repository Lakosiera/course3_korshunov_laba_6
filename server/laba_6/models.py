from django.db import models


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


class Deposit(models.Model):
    customer = models.ForeignKey(
        to=Customer,
        related_name='deposits',
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(
        verbose_name="Сумма",  # название столбца в админке и ошибках
        help_text="Сумма",
    )


class Loan(models.Model):
    customer = models.ForeignKey(
        to=Customer,
        related_name='loans',
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
        verbose_name="Выплата по",  # название столбца в админке и ошибках
        help_text="Выплата по",
    )
