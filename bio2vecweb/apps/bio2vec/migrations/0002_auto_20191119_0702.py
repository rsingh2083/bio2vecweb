# Generated by Django 2.0.8 on 2019-11-19 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio2vec', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='measurementTechnique',
            new_name='measurement_technique',
        ),
    ]
