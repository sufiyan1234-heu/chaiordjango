# Generated by Django 4.2.13 on 2024-05-22 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chaivarity',
            name='image',
        ),
        migrations.AlterField(
            model_name='chaivarity',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 22, 16, 39, 34, 780444, tzinfo=datetime.timezone.utc)),
        ),
    ]
