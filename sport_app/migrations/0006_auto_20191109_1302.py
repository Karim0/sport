# Generated by Django 2.2.6 on 2019-11-09 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport_app', '0005_auto_20191109_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='section_id',
            new_name='section',
        ),
    ]
