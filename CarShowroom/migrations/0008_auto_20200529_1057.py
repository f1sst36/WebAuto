# Generated by Django 3.0.5 on 2020-05-29 07:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarShowroom', '0007_auto_20200529_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='poster',
            field=models.TextField(verbose_name='Глав. изображение'),
        ),
        migrations.AlterField(
            model_name='purchasecar',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 29, 10, 57, 34, 901505), verbose_name='Дата записи'),
        ),
    ]