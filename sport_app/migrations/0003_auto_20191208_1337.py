# Generated by Django 3.0 on 2019-12-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_app', '0002_auto_20191208_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingsystem',
            name='workouts_per_week',
            field=models.TextField(null=True),
        ),
    ]
