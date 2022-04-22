from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .forms import addTaskForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
  form = addTaskForm(request.POST or None)
  context = {
    'posts': Post.objects.all(),
    'form': form
  }
  if request.method == 'POST':
    if form.is_valid():
      todo = form.save(commit=False)
      todo.author = request.user
      todo.save()
      messages.info(request, f'Task Added!')
      return redirect('home-page')
      
  return render(request, 'home.html', context)
  
  
@login_required
def about(request):
  return render(request, 'about.html')
  
  
@login_required
def profile(request):
  return render(request, 'profile.html')