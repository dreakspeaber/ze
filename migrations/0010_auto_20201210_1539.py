# Generated by Django 3.1.2 on 2020-12-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_remove_links_galeryheight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='facebook',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='twitter',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
    ]