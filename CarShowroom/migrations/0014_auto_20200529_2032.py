# Generated by Django 3.0.5 on 2020-05-29 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarShowroom', '0013_auto_20200529_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasecar',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 29, 20, 32, 47, 800530), verbose_name='Дата записи'),
        ),
        migrations.AlterField(
            model_name='servicecar',
            name='date_send',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 29, 20, 32, 47, 800530), verbose_name='Дата отправки заявки'),
        ),
    ]