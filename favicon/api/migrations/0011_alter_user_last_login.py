# Generated by Django 4.0.6 on 2022-07-25 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.TimeField(auto_now=True),
        ),
    ]
