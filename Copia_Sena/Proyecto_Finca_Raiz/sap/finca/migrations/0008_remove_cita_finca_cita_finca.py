# Generated by Django 4.2.3 on 2023-07-22 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finca', '0007_remove_finca_cita_cita_finca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cita',
            name='Finca',
        ),
        migrations.AddField(
            model_name='cita',
            name='finca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finca.finca'),
        ),
    ]
