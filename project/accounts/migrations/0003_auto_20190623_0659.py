# Generated by Django 2.0.13 on 2019-06-23 01:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20190620_2028'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Activity',
            new_name='PrefGenre',
        ),
        migrations.RenameField(
            model_name='prefgenre',
            old_name='activity',
            new_name='genre',
        ),
    ]
