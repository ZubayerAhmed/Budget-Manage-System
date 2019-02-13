from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from main_app.forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
import re

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'thank you.html')
        else:
            return HttpResponse("Username or password incorrect")
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

@login_required
def user_dashboard(request):
	return render(request,'thank you.html')
