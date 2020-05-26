from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

from .models import Profile


# Profile Inline admin descriptor
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


# New User Admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


# Re-register User Admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
