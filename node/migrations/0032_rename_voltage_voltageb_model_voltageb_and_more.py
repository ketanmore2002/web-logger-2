# Generated by Django 4.1.5 on 2023-07-31 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0031_rename_current_currentb_temp_currentb_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voltageb_model',
            old_name='voltage',
            new_name='voltageB',
        ),
        migrations.RenameField(
            model_name='voltager_model',
            old_name='voltage',
            new_name='voltageR',
        ),
        migrations.RenameField(
            model_name='voltagey_model',
            old_name='voltage',
            new_name='voltageY',
        ),
    ]
