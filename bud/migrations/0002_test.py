# Generated by Django 3.0.6 on 2020-05-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]