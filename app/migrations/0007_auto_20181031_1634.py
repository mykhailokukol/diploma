# Generated by Django 2.1.2 on 2018-10-31 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20181031_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='reserve_datetime',
            field=models.CharField(blank=True, default='-', max_length=40),
        ),
    ]