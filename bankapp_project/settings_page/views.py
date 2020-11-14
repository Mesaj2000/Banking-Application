from django.shortcuts import render, redirect
from view_balances.models import Account


def settings_page(request):
    if not request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        try:
            account_number = request.POST.get('account select radio', None)
            new = Account.objects.get(user=request.user, id=account_number)
            old = Account.objects.get(user=request.user, preferred=True)

            if new != old:
                old.preferred = False
                new.preferred = True
                old.save()
                new.save()

        except Exception as e:
            print("Exception!: ", str(e))

    accounts = Account.objects.filter(user=request.user).\
        order_by('account_type', 'id')

    preferred = Account.objects.get(user=request.user, preferred=True)

    context = {
        'accounts': accounts,
        'preferred': preferred
    }

    return render(request, 'settings_page/settings.html', context)
