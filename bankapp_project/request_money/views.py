from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from decimal import Decimal
from .models import Request
from datetime import datetime


def make_request(current_user, target_username, amount):
    try:
        target_user = User.objects.get(username=target_username)
    except Exception:
        raise Exception("Target user does not exist")

    new_request = Request(sender=current_user, receiver=target_user,
                          time=datetime.now(), amount=amount)

    new_request.save()


def request_money(request):
    if not request.user.is_authenticated:
        return redirect('index')

    context = {
        'error': False,
        'error_message': "",
        'sent': False
    }

    if request.method == 'POST':
        try:
            target_username = request.POST.get('target user field', None)

            """
            from_account_number = request.POST.get('from account radio', None)

            try:
                from_account_number = int(from_account_number)
            except Exception:
                raise Exception("Please select a sending account")
            """

            amount = request.POST.get('amount field', None)
            amount = Decimal(amount)

            make_request(request.user, target_username, amount)

            context['sent'] = True

        except Exception as e:
            context['error'] = True
            context['error_message'] = str(e)
            print(e)

    return render(request, 'request_money/request_money.html', context)


def view_requests(request, account_number=None):
    if not request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        try:
            delete_id = request.POST.get('delete', None)

            if delete_id is not None:
                to_delete = Request.objects.get(id=delete_id)

                if to_delete.receiver == request.user:
                    to_delete.delete()

        except Exception as e:
            print(e)

    requests = Request.objects.filter(receiver=request.user)

    context = {
        'requests': requests
    }

    return render(request, 'request_money/view_requests.html', context)
