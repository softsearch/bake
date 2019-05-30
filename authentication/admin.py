from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import User

class UserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username',]
    field = ('email', 'username',)

admin.site.register(User, UserAdmin)