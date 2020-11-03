from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=64)


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    preferred = models.BooleanField()


class Request(models.Model):
    sender = models.ForeignKey(User, related_name='sender',
                               on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver',
                                 on_delete=models.CASCADE)
    time = models.DateTimeField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)


class Transaction(models.Model):
    sender = models.ForeignKey(Account, related_name='sender',
                               on_delete=models.SET_NULL, null=True)
    receiver = models.ForeignKey(Account, related_name='receiver',
                                 on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
