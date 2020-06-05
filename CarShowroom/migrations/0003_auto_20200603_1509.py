# Generated by Django 3.0.5 on 2020-06-03 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarShowroom', '0002_auto_20200603_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasecar',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 3, 15, 9, 37, 469857), verbose_name='Дата записи'),
        ),
        migrations.AlterField(
            model_name='servicecar',
            name='date_send',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 3, 15, 9, 37, 470857), verbose_name='Дата отправки заявки'),
        ),
    ]