from django.db import models
from django.contrib.auth.models import User


# PROFILE
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    dp = models.ImageField(default='placeholders/usr/avatar-1577909.svg', verbose_name='Display Pic', blank=True,
                           upload_to='users/dp/')

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
