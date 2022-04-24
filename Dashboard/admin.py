from django.contrib import admin
from .models import Post, Profile
# Register your models here.
myModels = [Post, Profile]
admin.site.register(myModels)