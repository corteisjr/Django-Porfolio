# Generated by Django 3.1.1 on 2022-01-07 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myPortfolio', '0009_auto_20220107_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectos',
            name='created_on',
        ),
    ]