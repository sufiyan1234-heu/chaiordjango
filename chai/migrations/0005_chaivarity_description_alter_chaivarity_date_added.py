# Generated by Django 4.2.13 on 2024-05-22 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0004_alter_chaivarity_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='chaivarity',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 22, 17, 19, 19, 350997, tzinfo=datetime.timezone.utc)),
        ),
    ]