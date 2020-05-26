from django.contrib.auth.models import User
from django.db import models


# TODOBUD
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100, blank=False)
    is_complete = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
