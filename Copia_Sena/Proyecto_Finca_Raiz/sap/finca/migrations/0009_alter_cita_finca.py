# Generated by Django 4.2.3 on 2023-07-22 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finca', '0008_remove_cita_finca_cita_finca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='finca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finca.finca'),
        ),
    ]