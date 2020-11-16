from django.shortcuts import render, redirect
from .models import Account


# Very simple function, as "view balances" is just a static page
# The "request" parameter is the HTTP request recieved from the user's device
# The return value is a rendering of the page, an HttpResponse python object
def view_balances(request):
    # As always, redirect to login if the user isn't logged in
    if not request.user.is_authenticated:
        return redirect('index')

    # Get accounts from the database
    accounts = Account.objects.filter(user=request.user).\
        order_by('account_type', 'id')

    context = {'accounts': accounts}

    # Render the page
    print(request)
    print(render(request, 'view_balances/balances.html', context))
    return render(request, 'view_balances/balances.html', context)
