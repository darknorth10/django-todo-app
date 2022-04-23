from django import forms
from .models import Post
from django.forms import ModelForm
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