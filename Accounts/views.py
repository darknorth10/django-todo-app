from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def register(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      messages.info(request, f'Your account has been created. You can log in now!')
      return redirect('login-page')
    
  else:
    form = SignUpForm()
    messages.warning(request, f'Fill up the fields properly!')
    
  return render(request, 'register.html', {'form': form})

def login(request):
  return render(request,'login.html')