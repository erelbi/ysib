# Generated by Django 2.2.11 on 2020-03-22 09:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20200322_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emir',
            name='baslangic',
            field=models.DateField(default=datetime.datetime(2020, 3, 22, 9, 40, 29, 85891, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='emir',
            name='bitis',
            field=models.DateField(default=datetime.datetime(2020, 3, 22, 9, 40, 29, 85928, tzinfo=utc)),
        ),
    ]
