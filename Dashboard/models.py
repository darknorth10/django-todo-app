from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  date_created = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  
  def __str__(self):
    return self.title


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.png', upload_to='profile_pics')
  quote = models.CharField(max_length=200, blank=True, null=True)
  
  def __str__(self):
    return f'{self.user.username} Profile'
  