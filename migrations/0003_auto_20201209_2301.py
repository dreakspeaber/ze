# Generated by Django 3.1.2 on 2020-12-09 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='quali',
            field=models.CharField(max_length=100),
        ),
    ]
