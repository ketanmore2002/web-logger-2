# Generated by Django 4.1.5 on 2023-06-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0014_remove_time_stamp_parameter'),
    ]

    operations = [
        migrations.AddField(
            model_name='node_health',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='node_health',
            name='time',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]
