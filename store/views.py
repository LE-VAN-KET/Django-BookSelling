from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from verify_email.email_handler import send_verification_email


def home(request):
    return render(request, 'home.html')


def registration(request):
    form = RegistrationForm(request.POST or request.GET)
    if form.is_valid():
        # inactive_user = send_verification_email(request, form)
        # inactive_user.cleaned_data['email']
        form.save()
        return redirect('store:signin')

    return render(request, 'auth/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('store:index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('store:index')
            else:
                messages.error(request, 'username or password doesn\'t match')

    return render(request, "auth/signin.html")


def signout(request):
    logout(request)
    return redirect('store:index')
