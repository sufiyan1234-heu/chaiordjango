# Generated by Django 4.2.13 on 2024-05-22 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0008_alter_chaivarity_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaivarity',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 22, 17, 55, 47, 942200, tzinfo=datetime.timezone.utc)),
        ),
    ]
