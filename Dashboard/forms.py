from django import forms
from .models import Post, Profile
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView

#add task form
class addTaskForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = [
        'title',
        'content'
      ]

# update task form

class updateTaskForm(UpdateView):
  class Meta:
    model = Post
    fields = [
        'title',
        'content'
      ]
      
# update profile
class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
  first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
  class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        
class updateProfile(forms.ModelForm):
  image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
  quote = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
  
  class Meta:
        model = Profile
        fields = ['image', 'quote']