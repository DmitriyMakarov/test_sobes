import json
import string
import random

from django.core import serializers
from django.forms.models import model_to_dict
from django.db import models
import uuid

from django.db.models import Sum


# Create your models here.
def new_account_number():
    return ''.join(random.choice(string.digits) for _ in range(20))

class PaymentAccountModel(models.Model):
    """Payment Account model"""
    CURRENCY_CHOICES = (
        ("RUB", "Российский Рубль"),
        ("USD", "Доллар США"),
    )


    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    account_number = models.CharField("Номер счета", max_length=20, null=False, blank=False, default=new_account_number())
    currency = models.CharField("Валюта счета", max_length=3, null=False, choices=CURRENCY_CHOICES)

    def __str__(self):
        return self.account_number


    @property
    def balance(self):
        to_sum = TransactionModel.objects.filter(to_acc=self.pk).aggregate(Sum("sum"))["sum__sum"]
        from_sum = TransactionModel.objects.filter(from_acc=self.pk).aggregate(Sum("sum"))["sum__sum"]
        if to_sum is None:
            to_sum = 0.0
        if from_sum is None:
            from_sum  = 0.0
        return to_sum - from_sum

    @property
    def get_from_transactions_list(self):
        obj = TransactionModel.objects.filter(from_acc=self.pk).all()
        return serializers.serialize('json', obj)

    @property
    def get_in_transactions_list(self):
        obj = TransactionModel.objects.filter(to_acc=self.pk).all()
        return serializers.serialize('json', obj)



class TransactionModel(models.Model):
    """Transaction model"""
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    from_acc = models.ForeignKey("PaymentAccountModel", on_delete=models.CASCADE, related_name="from_acc_transaction")
    to_acc = models.ForeignKey("PaymentAccountModel", on_delete=models.CASCADE, related_name="to_acc_transaction")
    sum = models.FloatField("Сумма транзации", null=True, blank=True)

    def __str__(self):
        return self.uuid