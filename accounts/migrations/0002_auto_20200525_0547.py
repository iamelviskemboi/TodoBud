# Generated by Django 3.0.6 on 2020-05-25 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dp',
            field=models.ImageField(blank=True, default='placeholders/usr/avatar-1577909.svg', null=True, upload_to='users/dp/', verbose_name='Display Pic'),
        ),
    ]
