# Generated by Django 3.0.5 on 2020-06-03 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarShowroom', '0007_auto_20200603_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticinfo',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='purchasecar',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 3, 17, 2, 37, 924676), verbose_name='Дата записи'),
        ),
        migrations.AlterField(
            model_name='servicecar',
            name='date_send',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 3, 17, 2, 37, 925676), verbose_name='Дата отправки заявки'),
        ),
    ]