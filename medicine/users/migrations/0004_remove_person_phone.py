# Generated by Django 4.1.3 on 2022-11-09 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_phone_number_person_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='phone',
        ),
    ]
