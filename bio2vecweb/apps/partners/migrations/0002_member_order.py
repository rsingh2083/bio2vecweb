# Generated by Django 2.0.8 on 2018-10-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]