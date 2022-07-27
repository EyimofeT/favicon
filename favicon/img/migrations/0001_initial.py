# Generated by Django 4.0.6 on 2022-07-26 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('created_at', models.CharField(default=datetime.datetime(2022, 7, 26, 14, 28, 18, 871446), max_length=200)),
            ],
        ),
    ]
