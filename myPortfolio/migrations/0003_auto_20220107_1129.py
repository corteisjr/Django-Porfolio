# Generated by Django 3.1.1 on 2022-01-07 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myPortfolio', '0002_auto_20220107_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectos',
            options={'ordering': ('-publish',)},
        ),
    ]
