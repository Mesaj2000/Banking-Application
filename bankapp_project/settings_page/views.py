from django.shortcuts import render, redirect
from view_balances.models import Account

# The "request" parameter is the HTTP request recieved from the user's device
# The return value is a rendering of the page, an HttpResponse python object
def settings_page(request):
    # As always, redirect if the user isn't logged in
    if not request.user.is_authenticated:
        return redirect('index')

    # If the user is trying to change their preferred account...
    if request.method == "POST":
        try:
            # ... get the selected account ID from the radio button...
            account_number = request.POST.get('account select radio', None)
            new = Account.objects.get(user=request.user, id=account_number)

            # ... and their currently preferred account...
            old = Account.objects.get(user=request.user, preferred=True)

            # ... and so long as a change needs to me made...
            if new != old:
                # ... switch which one is preferred...
                old.preferred = False
                new.preferred = True

                # ... making sure to record the change in the database
                old.save()
                new.save()

        except Exception as e:
            # Something weird happened; mostly only possible if they're
            # meddeling with the POST
            print("Exception!: ", str(e))

    # Load the accounts from the database so we can put them in the
    # radio buttons.
    accounts = Account.objects.filter(user=request.user).\
        order_by('account_type', 'id')

    # Load the preferred account from the database so we can let the
    # user know which is currently selected.
    preferred = Account.objects.get(user=request.user, preferred=True)

    context = {
        'accounts': accounts,
        'preferred': preferred
    }

    return render(request, 'settings_page/settings.html', context)
