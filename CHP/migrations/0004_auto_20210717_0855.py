# Generated by Django 3.2.4 on 2021-07-17 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CHP', '0003_auto_20210717_0818'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorie',
            new_name='Categories',
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]