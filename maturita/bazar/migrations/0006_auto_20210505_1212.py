# Generated by Django 3.2.1 on 2021-05-05 10:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazar', '0005_auto_20210505_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='spotreba',
            field=models.FloatField(help_text='Zadej prumernou spotrebu', null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Průměrná spotřeba'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='sila',
            field=models.FloatField(help_text='Zadej pocet konskych sil', null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Počet koní'),
        ),
    ]
