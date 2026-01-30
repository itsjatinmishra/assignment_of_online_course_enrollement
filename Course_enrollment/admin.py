from django.contrib import admin

from .models import User, Course, Module, Enrollment
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Enrollment)
