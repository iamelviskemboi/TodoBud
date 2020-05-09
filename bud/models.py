from django.db import models


# TODOBUD
class Todo(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content
