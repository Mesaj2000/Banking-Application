from django.shortcuts import render
from .models import Account


def view_balances(request):
    accounts = Account.objects.filter(user=request.user)
    context = {'accounts': accounts}
    return render(request, 'view_balances/balances.html', context)
