# Generated by Django 2.1.4 on 2019-01-29 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_sensor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
