# Generated by Django 4.1.5 on 2023-07-31 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0032_rename_voltage_voltageb_model_voltageb_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentb_model',
            old_name='current',
            new_name='currentB',
        ),
        migrations.RenameField(
            model_name='currentr_model',
            old_name='current',
            new_name='currentR',
        ),
        migrations.RenameField(
            model_name='currenty_model',
            old_name='current',
            new_name='currentY',
        ),
    ]