# Generated by Django 2.2.6 on 2019-11-11 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport_app', '0006_auto_20191109_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='location',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='sport_app.Location'),
            preserve_default=False,
        ),
    ]
