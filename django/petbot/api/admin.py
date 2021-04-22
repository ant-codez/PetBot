from django.contrib import admin
from .models import User, Pet

# Register your models here.
admin.site.register(User)
admin.site.register(Pet)