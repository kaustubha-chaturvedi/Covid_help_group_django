# Generated by Django 3.2.4 on 2021-07-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('CHP', '0008_alter_user_usergroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='usergroup',
        ),
        migrations.AddField(
            model_name='user',
            name='usergroup',
            field=models.ManyToManyField(blank=True, null=True, related_name='groups', to='auth.Group'),
        ),
    ]