# Generated by Django 4.1.3 on 2022-11-29 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_appointments_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='patient',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='main.patient'),
        ),
    ]