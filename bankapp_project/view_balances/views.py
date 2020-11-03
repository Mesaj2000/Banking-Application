from django.shortcuts import render
from .models import Account


def view_balances(request):
    # user = User.objects.get(username=)
    checking = Account.objects.filter(user=request.user,
                                      account_type="Checking").get()
    savings = Account.objects.filter(user=request.user,
                                     account_type="Savings").get()
    context = {
        'checking': checking,
        'savings': savings
        }

    return render(request, 'view_balances/balances.html', context)
