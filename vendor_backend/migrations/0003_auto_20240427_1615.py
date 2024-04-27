# Generated by Django 3.2.23 on 2024-04-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_backend', '0002_activityheatmapdata_gotolocationrequest_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegionalDataHeatmap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.TextField()),
                ('total_activity', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='gotolocationrequest',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='gotolocationrequest',
            name='longitude',
        ),
        migrations.AddField(
            model_name='gotolocationrequest',
            name='region',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]