# Generated by Django 2.0.6 on 2018-12-10 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20181210_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsimage',
            name='add_image',
            field=models.DateField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]
