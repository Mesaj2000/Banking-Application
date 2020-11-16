from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


# Simply renders the index.html page
# Since the index is static, no context is needed
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'authentication_system/index.html')


# For GET requests, simply create a UserCreationForm and renders it.
# For POST requests, take the input from the UserCreationForm and extract 
# out the login credentials. If they are valid, the user logs into the system.
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

            # Redirect to the front page
            return redirect('index')

    else:
        # Generate a fresh form
        form = UserCreationForm()

    # Either way, render the form for the user to see
    context = {'form': form}
    return render(request, 'registration/register.html', context)
