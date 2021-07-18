# Generated by Django 3.1.7 on 2021-07-18 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CHP', '0005_auto_20210718_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='CHP.categories')),
            ],
        ),
    ]
