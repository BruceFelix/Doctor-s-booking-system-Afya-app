# Generated by Django 4.1.3 on 2022-11-29 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_appointment_appointments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='doctor',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='main.doctor'),
        ),
    ]