from django.contrib import admin
from .models import Todo


# Todobud
class TodoAdmin(admin.ModelAdmin):
    list_display = ['content']


admin.site.register(Todo, TodoAdmin)
