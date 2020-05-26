from django import forms

from .models import Task


# Add Todos
class TodoAddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
