# Generated by Django 2.2.8 on 2020-01-03 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_create_apartment_sensor_attributes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentsensorvalue',
            name='apartment_sensor',
        ),
        migrations.RemoveField(
            model_name='apartmentsensorvalue',
            name='attribute',
        ),
    ]