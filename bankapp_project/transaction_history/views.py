
from django.shortcuts import render, redirect
from .models import Transaction
from view_balances.models import Account


def transaction_history(request, account_number=None):
    if not request.user.is_authenticated:
        return redirect('index')

    accounts = Account.objects.filter(user=request.user).\
        order_by('account_type', 'id')

    if request.method == "POST":
        try:
            account_number = request.POST.get('account select radio', None)
            account = Account.objects.get(user=request.user, id=account_number)
        except Exception as e:
            account = accounts[0]
            print(e)
            print(account_number)

    else:
        account = accounts[0]

    transactions = (Transaction.objects.filter(sender=account) |
                    Transaction.objects.filter(receiver=account))

    context = {
        'selected': account,
        'accounts': accounts,
        'transactions': transactions
    }

    return render(request, 'transaction_history/transactions.html', context)
