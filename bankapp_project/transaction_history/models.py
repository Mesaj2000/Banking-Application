from django.db import models
# from django.contrib.auth.models import User
from view_balances.models import Account


class Transaction(models.Model):
    sender = models.ForeignKey(Account, related_name='sender',
                               on_delete=models.SET_NULL, null=True)
    receiver = models.ForeignKey(Account, related_name='receiver',
                                 on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
