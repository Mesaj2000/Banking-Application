from django.db import models
from django.contrib.auth.models import User


class Request(models.Model):
    sender = models.ForeignKey(User, related_name='sender',
                               on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver',
                                 on_delete=models.CASCADE)
    time = models.DateTimeField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
