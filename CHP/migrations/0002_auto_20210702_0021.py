# Generated by Django 3.2.4 on 2021-07-01 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CHP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='Icon',
            new_name='icon',
        ),
        migrations.RenameField(
            model_name='categories',
            old_name='Name',
            new_name='name',
        ),
    ]
