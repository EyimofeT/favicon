# Generated by Django 4.0.6 on 2022-07-25 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_user_firstname_remove_user_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.TimeField(auto_now_add=True),
        ),
    ]