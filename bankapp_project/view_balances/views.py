from django.shortcuts import render, redirect
from .models import Account


def view_balances(request):
    if not request.user.is_authenticated:
        return redirect('index')

    accounts = Account.objects.filter(user=request.user)
    context = {'accounts': accounts}

    return render(request, 'view_balances/balances.html', context)
