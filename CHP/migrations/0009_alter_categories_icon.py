# Generated by Django 3.2.4 on 2021-07-31 05:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CHP', '0008_alter_categories_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='icon',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
