from django.db import models
from django.contrib.auth.models import User
from enum import Enum


# There are only two account types: Checking and Savings
# This inherits from the Enum class, which is how you make an Enum in python
class Account_Type(Enum):
    CHECKING = "Checking"
    SAVINGS = "Savings"


# A bank account database entry
# Each user has multiple accouts, one of which is preferred
# Each transaction has two accounts, a sender and a receiver
# As this is a database entry for a Django web application,
#   it inherits from the models.Model class in Django.
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
