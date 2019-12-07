# Generated by Django 2.2.6 on 2019-12-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_app', '0003_auto_20191202_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingsystem',
            name='aim',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='trainingsystem',
            name='cycle_duration',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='trainingsystem',
            name='time',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='trainingsystem',
            name='workouts_per_week',
            field=models.IntegerField(null=True),
        ),
    ]