# Generated by Django 4.2.3 on 2023-07-21 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finca', '0005_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='finca',
            name='cita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finca.cita'),
        ),
    ]
