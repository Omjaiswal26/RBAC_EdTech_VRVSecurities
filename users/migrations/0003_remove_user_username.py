# Generated by Django 5.1.3 on 2024-11-28 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
