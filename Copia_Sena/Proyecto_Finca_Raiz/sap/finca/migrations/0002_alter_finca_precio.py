# Generated by Django 4.2.3 on 2023-07-19 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finca',
            name='precio',
            field=models.CharField(max_length=255),
        ),
    ]
