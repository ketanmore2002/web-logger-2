# Generated by Django 4.1.5 on 2023-07-20 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0023_delete_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodes_model',
            name='date',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='nodes_model',
            name='time',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
