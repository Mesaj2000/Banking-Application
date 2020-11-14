from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from view_balances.models import Account
from decimal import Decimal
from transaction_history.models import Transaction
from datetime import datetime


def transaction(current_user, target_username, from_account_number, amount):
    try:
        target_user = User.objects.get(username=target_username)
        target_account = Account.objects.get(user=target_user, preferred=True)
    except Exception:
        raise Exception("Target user does not exist")

    try:
        from_account = Account.objects.get(user=current_user,
                                           id=from_account_number)
    except Exception:
        raise Exception("Invalid selected sending account")

    if from_account.balance < amount:
        raise Exception("Insufficient funds")

    if from_account == target_account:
        raise Exception("Nebulous transaction ignored")

    from_account.balance -= amount
    target_account.balance += amount
    transaction = Transaction(sender=from_account, receiver=target_account,
                              time=datetime.now(), amount=amount)

    from_account.save()
    target_account.save()
    transaction.save()


def send_money(request):
    if not request.user.is_authenticated:
        return redirect('index')

    accounts = Account.objects.filter(user=request.user).\
        order_by('account_type', 'id')

    context = {
        'error': False,
        'error_message': "",
        'sent': False,
        'accounts': accounts
    }

    if request.method == 'POST':
        try:
            target_username = request.POST.get('target user field', None)

            from_account_number = request.POST.get('from account radio', None)

            try:
                from_account_number = int(from_account_number)
            except Exception:
                raise Exception("Please select a sending account")

            amount = request.POST.get('amount field', None)
            amount = Decimal(amount)

            transaction(request.user, target_username,
                        from_account_number, amount)

            context['sent'] = True

        except Exception as e:
            context['error'] = True
            context['error_message'] = str(e)
            print(e)

    return render(request, 'send_money/send_money.html', context)
