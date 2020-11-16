from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from decimal import Decimal
from .models import Request
from datetime import datetime


# Unlike transactions, requests don't involve changing any
# existing information, only adding something to the database.
# This function handles all the data validation for user-entered data
def make_request(current_user, target_username, amount):
    # Make sure the requested user exists in the database
    try:
        target_user = User.objects.get(username=target_username)
    except Exception:
        raise Exception("Target user does not exist")

    # Make sure the entered amount is a valid number
    try:
        amount = Decimal(amount)
    except Exception:
        raise Exception("Invalid entered amount")

    # Generate a new "money request" database entry
    new_request = Request(sender=current_user, receiver=target_user,
                          time=datetime.now(), amount=amount)

    # Save it to the database
    new_request.save()


# Renders the "request money" page, and processes user input
# The "request" parameter is the HTTP request recieved from the user's device
# The return value is a rendering of the page, an HttpResponse python object
def request_money(request):
    # As always, redirect elsewhere if the user isn't logged in
    if not request.user.is_authenticated:
        return redirect('index')

    # Unless otherwise indicated, there are no
    # errors and nothing has been sent
    context = {
        'error': False,
        'error_message': "",
        'sent': False
    }

    # POST means the user gave us some information in the form,
    # so we gotta parse it and potentially update the database
    # with the new request
    if request.method == 'POST':
        try:
            # Grab from the form the person from
            # which the user is requesting money
            target_username = request.POST.get('target user field', None)

            # Grab the amount of money they would like to request
            amount = request.POST.get('amount field', None)

            # Generate the request and add it to the database if valid
            make_request(request.user, target_username, amount)

            # If we make it here, there weren't any exceptions.
            # That means it worked, so we can let the user know
            context['sent'] = True

        except Exception as e:
            # Something went wrong
            # Notify the user what it is, and print it to the console too
            context['error'] = True
            context['error_message'] = str(e)
            print(e)

    # If it wasn't a POST request, the initial context is displayed as-is
    # If it was a POST request, the contex would be modified in some way
    return render(request, 'request_money/request_money.html', context)


# Renders the "view requests" page, and processes user input
# The "request" parameter is the HTTP request recieved from the user's device
# The return value is a rendering of the page, an HttpResponse python object
def view_requests(request, account_number=None):
    # As always, redirect elsewhere if the user isn't logged in
    if not request.user.is_authenticated:
        return redirect('index')

    # The only POST information is whether they
    # pushed one of the delete buttons
    if request.method == "POST":
        try:
            # Get the id of the request they selected to delete
            delete_id = request.POST.get('delete', None)

            # Make sure that the user actually clicked the button
            # and didn't post some other way
            if delete_id is not None:
                # Get the database entry with that id
                to_delete = Request.objects.get(id=delete_id)

                # Users can only delete requests made to them
                # Just a safety precausion; shouldn't actually come up
                # in proper use of the system.
                if to_delete.receiver == request.user:
                    # Remove it from the database
                    to_delete.delete()

        except Exception as e:
            # If something goes wrong, dump it in the
            # console but don't change anything
            print(e)

    # Get all the requests made TO the currently logged-in user
    requests = Request.objects.filter(receiver=request.user)

    # Render the page with those requests in the table
    context = {'requests': requests}
    return render(request, 'request_money/view_requests.html', context)
