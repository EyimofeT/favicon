# Generated by Django 4.0.6 on 2022-07-25 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_user_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]