
from django.shortcuts import render, redirect
from .models import Transaction
from view_balances.models import Account


def transaction_history(request, account_number=None):
    # As always, redirect to login if the user isn't logged in
    if not request.user.is_authenticated:
        return redirect('index')

    # Need to get the accounts so we can present them in the selection radio
    accounts = Account.objects.filter(user=request.user).\
        order_by('account_type', 'id')

    # If the user wishes to change the selected account...
    if request.method == "POST":
        try:
            # ... load the account from the database.
            account_number = request.POST.get('account select radio', None)
            account = Account.objects.get(user=request.user, id=account_number)
        except Exception as e:
            # If there's a problem, default to the first account
            account = accounts[0]
            print(e)
            print(account_number)

    # Othewise...
    else:
        # ... default to the "first" account.
        account = accounts[0]

    # Get all the transactions that were sent
    # either to or from the selected account.
    transactions = (Transaction.objects.filter(sender=account) |
                    Transaction.objects.filter(receiver=account))

    # Gather all relevant information...
    context = {
        'selected': account,
        'accounts': accounts,
        'transactions': transactions
    }

    # ... and present it to the user.
    return render(request, 'transaction_history/transactions.html', context)
