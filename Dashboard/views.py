from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post, Profile
from .forms import addTaskForm, updateTaskForm, updateProfile, UserUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
  # Add Task form
  form = addTaskForm(request.POST or None)
  # Update task form
  # Dictionary
  context = {
    'posts': Post.objects.all(),
    'form': form
  }
  # Add task
  if request.method == 'POST':
    if form.is_valid():
      todo = form.save(commit=False)
      todo.author = request.user
      todo.save()
      messages.info(request, f'Task Added!')
      return redirect('home-page')
      
  return render(request, 'home.html', context)
  
  #update task
@login_required
def update_task(request, id):
  context ={}
  obj = get_object_or_404(Post, id = id)
  form = addTaskForm(request.POST or None, instance = obj)
  if form.is_valid():
    form.save()
    messages.success(request, f'Task Updated Successfully!')
    return redirect('home-page')
  
  context["form"] = form
  return render(request, "updateTask.html", context)
  
  #Delete Task
def delete_task(request, id):
  obj = get_object_or_404(Post, id = id)
  
  if request.method == 'POST':
    obj.delete()
    messages.warning(request, f'Task has been deleted')
    return redirect('home-page')
  return render(request, "delete.html")
  
  
@login_required
def profile(request):
  context = {
    'profiles': Profile.objects.all(),
  }
  return render(request, 'profile.html', context)


# update Profile
def update_profile(request):
  user_form = UserUpdateForm(request.POST, instance=request.user)
  profile_form = updateProfile(request.POST, request.FILES, instance=request.user.profile)
  if request.method == 'POST':
    
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, 'Your profile is updated successfully')
      return redirect(to='profile-page')
    else:
      user_form = UserUpdateForm(instance=request.user)
      profile_form = updateProfile(instance=request.user.profile)
  return render(request, 'updateProfile.html', {'user_form': user_form, 'profile_form': profile_form})
  