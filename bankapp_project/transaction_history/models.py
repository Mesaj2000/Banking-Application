from django.db import models
from view_balances.models import Account


# A bank transaction database entry
# Each transaction has two accounts, a sender and a receiver
# As this is a database entry for a Django web application,
#   it inherits from the models.Model class in Django.
class Transaction(models.Model):
    # The account from which the money was sent
    sender = models.ForeignKey(Account, related_name='sender',
                               on_delete=models.SET_NULL, null=True)

    # The account to which the money was sent
    receiver = models.ForeignKey(Account, related_name='receiver',
                                 on_delete=models.SET_NULL, null=True)

    # When the money was sent
    time = models.DateTimeField()

    # How much money was sent
    amount = models.DecimalField(max_digits=6, decimal_places=2)
