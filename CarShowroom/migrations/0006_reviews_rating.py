# Generated by Django 3.0.5 on 2020-05-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarShowroom', '0005_testdrive_send_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='rating',
            field=models.PositiveSmallIntegerField(default=3, verbose_name='Рейтинг отзыва'),
        ),
    ]
