# Generated by Django 3.2.4 on 2021-09-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CHP', '0013_alter_alldata_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alldata',
            old_name='address1',
            new_name='address',
        ),
        migrations.AddField(
            model_name='alldata',
            name='landmark',
            field=models.TextField(blank=True, null=True),
        ),
    ]