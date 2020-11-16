from django.db import models
from view_balances.models import Account


# A database entry for a trasaction contains:
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
