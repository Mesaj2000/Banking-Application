from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from view_balances.models import Account


# Simply renders the index.html page
# Since the index is static, no context is needed
# The "request" parameter is the HTTP request recieved from the user's device
# The return value is a rendering of the page, an HttpResponse python object
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'authentication_system/index.html')


# For GET requests, simply create a UserCreationForm and renders it.
# For POST requests, take the input from the UserCreationForm and extract
# out the login credentials. If they are valid, the user logs into the system.
# The "request" parameter is the HTTP request recieved from the user's device
# The return value is a rendering of the page, an HttpResponse python object
def register(request):
    if request.method == 'POST':
        # Load user's form info that they sent in the post
        form = UserCreationForm(request.POST)

        # Check to make sure they didn't enter bad inputs
        if form.is_valid():
            form.save()

            # Clean up the data to avoid malicious activity (mostly XSS)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Validate the credentials, and log in if they're correct
            user = authenticate(username=username, password=password)
            login(request, user)

            # Generate a new checking account and savings account for the user
            checking = Account(user=user, balance=100,
                               preferred=True, account_type="Checking")
            savings = Account(user=user, balance=100,
                              preferred=False, account_type="Savings")

            # Save the new accounts to the database
            checking.save()
            savings.save()

            # Redirect to the front page
            return redirect('index')

    else:
        # Generate a fresh form
        form = UserCreationForm()

    # Either way, render the form for the user to see
    context = {'form': form}
    return render(request, 'registration/register.html', context)
