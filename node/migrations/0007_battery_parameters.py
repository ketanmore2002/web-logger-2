# Generated by Django 4.1.5 on 2023-06-19 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0006_current_parameters_generator_speed_parameters_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='battery_parameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=300, null=True)),
                ('battery', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
