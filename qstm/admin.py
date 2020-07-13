from django.contrib import admin
from .models import (
    User,
    Parent,
    Student,
    Task,
    Site,
)

# Register your models here.
admin.site.register(User)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Task)
admin.site.register(Site)
