# Generated by Django 4.2.13 on 2024-05-22 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0006_alter_chaivarity_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaivarity',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 22, 17, 51, 14, 293639, tzinfo=datetime.timezone.utc)),
        ),
    ]