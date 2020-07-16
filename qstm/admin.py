from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import (
    # User,
    CustomUser,
    Parent,
    Student,
    Task,
    Site,
)

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'password']

admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(User)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Task)
admin.site.register(Site)
