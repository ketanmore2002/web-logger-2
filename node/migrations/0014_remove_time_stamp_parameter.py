# Generated by Django 4.1.5 on 2023-06-24 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0013_remove_node_health_date_remove_node_health_date_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time_stamp',
            name='parameter',
        ),
    ]