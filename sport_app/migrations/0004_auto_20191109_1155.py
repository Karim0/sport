# Generated by Django 2.2.6 on 2019-11-09 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport_app', '0003_auto_20191104_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_app.SportSection')),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
