from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from view_balances.models import Account
from decimal import Decimal
from transaction_history.models import Transaction
from datetime import datetime

# Takes in:
#   The current user
#   The username of the user they want to send money to (as a string)
#   The number of the selected account the money is coming from (as a string)
#   The amount of money the user would like to send (as a string)
# Converts all strings into appropriate values / database entires
# Generates a new Transaction database entry
# Updates the balances of the sending and recieving accounts
# Saves all new or updated database entreis
def transaction(current_user, target_username, from_account_number, amount):
    # Parse user input for the user to which they are sending money,
    # then load that user's preferred account from the database.
    # If any of this isn't possible, inform the user of the error.
    try:
        target_user = User.objects.get(username=target_username)
        target_account = Account.objects.get(user=target_user, preferred=True)
    except Exception:
        raise Exception("Target user does not exist")

    # Parse the radio button response for the account number of the account
    # from which the money is to be sent, then load account from the database.
    # If this fails somehow, inform the user of the error.
    try:
        from_account_number = int(from_account_number)
        from_account = Account.objects.get(user=current_user,
                                           id=from_account_number)
    except Exception:
        raise Exception("Invalid selected sending account")

    # Parse the user input for the amount of money they would like to send.
    # If the entered amount isn't valid, inform the user of the error.
    try:
        amount = Decimal(amount)
    except Exception:
        raise Exception("Invalid entered amount")

    # Verify that the selected account has enough money to send.
    if from_account.balance < amount:
        raise Exception("Insufficient funds")

    # Verify that the selected account and the target account aren't the same,
    # which would be entirely pointless to transact.
    if from_account == target_account:
        raise Exception("Nebulous transaction ignored")

    # If all the inputs are valid, update the account balances by the amount
    # given, and generate a new Transaction database entry.
    from_account.balance -= amount
    target_account.balance += amount
    transaction = Transaction(sender=from_account, receiver=target_account,
                              time=datetime.now(), amount=amount)

    # Save all the changes to to database.
    from_account.save()
    target_account.save()
    transaction.save()


# Loads the view for the user to see with all relevant 
# informtion for sending money
def send_money(request):
    # As always, if the user isn't logged in, redirect them to login
    if not request.user.is_authenticated:
        return redirect('index')

    # Retrieve the user's bank accounts from the database so that
    # they can be displayed in the radio buttons.
    accounts = Account.objects.filter(user=request.user).\
        order_by('account_type', 'id')

    # By default, there are no errors and nothing is being sent
    context = {
        'error': False,
        'error_message': "",
        'sent': False,
        'accounts': accounts
    }

    # If the user is POST-ing information (meaning: they sent money)...
    if request.method == 'POST':
        try:
            # ... pull the information from each of the form fields and...
            target_username = request.POST.get('target user field', None)
            from_account_number = request.POST.get('from account radio', None)
            amount = request.POST.get('amount field', None)

            # ... make a transaction with it.
            transaction(request.user, target_username,
                        from_account_number, amount)

            context['sent'] = True

        # If there are errors, forward them to the user to display as an alert.
        except Exception as e:
            context['error'] = True
            context['error_message'] = str(e)
            print(e)

    # Always render the page with the provided context
    return render(request, 'send_money/send_money.html', context)
