from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client
# Register your models here.
from .forms import CustomUserCreation, CustomUserChange


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    change = CustomUserChange
    model = Client


admin.site.register(Client, CustomUserAdmin)
