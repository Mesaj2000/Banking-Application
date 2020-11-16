from django.db import models
from django.contrib.auth.models import User


# A request has:
#   the USER that made the request
#   the USER the request was made to
#   the timestamp of when the request was made
#   the amount of money the request is for
class Request(models.Model):
    sender = models.ForeignKey(User, related_name='sender',
                               on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver',
                                 on_delete=models.CASCADE)
    time = models.DateTimeField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
