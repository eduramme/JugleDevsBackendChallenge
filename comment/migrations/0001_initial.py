# Generated by Django 3.0.7 on 2021-03-03 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Name', max_length=100)),
                ('content', models.CharField(default='Name', max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 3, 3, 5, 0, 8, 373641), verbose_name='date published')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2021, 3, 3, 5, 0, 8, 373661), verbose_name='date updated')),
            ],
        ),
    ]
