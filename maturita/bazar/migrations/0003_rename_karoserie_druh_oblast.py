# Generated by Django 3.2.1 on 2021-05-05 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bazar', '0002_alter_auto_stav'),
    ]

    operations = [
        migrations.RenameField(
            model_name='druh',
            old_name='karoserie',
            new_name='oblast',
        ),
    ]
