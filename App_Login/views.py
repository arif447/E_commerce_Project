from django.shortcuts import render, HttpResponseRedirect
from django.urls import path, reverse
from django.http import HttpRequest, HttpResponse

# import forms and model
from App_Login.models import User, Profile
from App_Login.forms import Singup_Form, profile_form

# Authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Messages
from django.contrib import messages




# Create your views here.
def sign_up(request):
    form = Singup_Form()
    if request.method == 'POST':
        form = Singup_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Create account successfully")
            return HttpResponseRedirect(reverse('App_Login:login'))
    diction = {'form': form}
    return render(request, 'App_Login/singup_Form.html', context=diction)

def user_login(request):
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully login")
                return HttpResponseRedirect(reverse('App_Shop:home'))
    diction = {'form': form}
    return render(request, 'App_Login/login_Form.html', context=diction)

@login_required()
def user_logout(request):
    logout(request)
    messages.warning(request, "You are logged out")
    return HttpResponseRedirect(reverse('App_Shop:home'))

@login_required()
def user_profile(request):
    profile = Profile.objects.get(user=request.user)

    form = profile_form(instance=profile)
    if request.method == 'POST':
        form = profile_form(request.POST, instance=profile,)
        if form.is_valid():
            form.save()
            form = profile_form(instance=profile)
            messages.success(request, "Changed save")
    diction = {'form': form}
    return render(request, 'App_Login/change_profile.html', context=diction)

