from django.contrib import admin
from .models import Task


# Todobud
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Task, TaskAdmin)
