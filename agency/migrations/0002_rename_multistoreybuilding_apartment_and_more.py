# Generated by Django 4.1.6 on 2023-03-07 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MultiStoreyBuilding',
            new_name='Apartment',
        ),
        migrations.RenameField(
            model_name='flat',
            old_name='home',
            new_name='apartment',
        ),
    ]
