from django.db import models
from django.contrib.auth.models import User
from enum import Enum


# There are only two account types: Checking and Savings
class Account_Type(Enum):
    CHECKING = "Checking"
    SAVINGS = "Savings"


# An account database entry has:
class Account(models.Model):
    # The user who owns the account
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # The amount of money currently in the account
    balance = models.DecimalField(max_digits=6, decimal_places=2)

    # Whether the account is "preferred"
    # The preferred account is where money is sent by other users
    preferred = models.BooleanField()

    # The account type: Checking or Savings
    account_type = models.CharField(max_length=10,
                                    choices=[(tag, tag.value)
                                             for tag in Account_Type])
