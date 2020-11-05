from django.shortcuts import render
from django.contrib.auth.models import User
from view_balances.models import Account
from decimal import Decimal


def transaction(target_username, from_account_number, amount):

    try:
        target_user = User.objects.get(username=target_username)
        target_account = Account.objects.get(user=target_user, preferred=True)
    except Exception:
        raise Exception("Target user does not exist")

    try:
        from_account = Account.objects.get(id=from_account_number)
    except Exception:
        raise Exception("'From account' does not exist")

    if from_account.balance < amount:
        raise Exception("Insufficient funds")

    from_account.balance -= amount
    target_account.balance += amount

    from_account.save()
    target_account.save()


def send_money(request):
    accounts = Account.objects.filter(user=request.user)

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
            from_account_number = int(from_account_number)

            amount = request.POST.get('amount field', None)
            amount = Decimal(amount)

            transaction(target_username, from_account_number, amount)

            """
            target_user = User.objects.get(username=target_username)
            target_account = Account.objects.get(user=target_user,
                                                 preferred=True)

            print(target_account)
            print(amount)
            print(type(amount))
            target_account.balance += amount
            print('how about here?')
            target_account.save()
            """

            context['sent'] = True

        except Exception as e:
            context['error'] = True
            context['error_message'] = str(e)
            print(e)

    return render(request, 'send_money/send_money.html', context)
