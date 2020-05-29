# Generated by Django 3.0.5 on 2020-05-29 20:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarShowroom', '0014_auto_20200529_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasecar',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 29, 23, 6, 6, 412522), verbose_name='Дата записи'),
        ),
        migrations.AlterField(
            model_name='servicecar',
            name='date_send',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 29, 23, 6, 6, 413522), verbose_name='Дата отправки заявки'),
        ),
    ]
