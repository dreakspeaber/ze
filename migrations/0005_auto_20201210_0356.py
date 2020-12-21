# Generated by Django 3.1.2 on 2020-12-10 03:56

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20201209_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.FileField(blank=True, upload_to=web.models.logoPath),
        ),
        migrations.AlterField(
            model_name='intro',
            name='image',
            field=models.FileField(blank=True, upload_to=web.models.logoPath),
        ),
    ]