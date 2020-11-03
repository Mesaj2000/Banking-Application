from django.db import models
from django.contrib.auth.models import User
from enum import Enum


class Account_Type(Enum):
    CHECKING = "Checking"
    SAVINGS = "Savings"


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    preferred = models.BooleanField()
    account_type = models.CharField(max_length=10,
                                    choices=[(tag, tag.value)
                                             for tag in Account_Type])
