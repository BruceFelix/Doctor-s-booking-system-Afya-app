# Generated by Django 4.1.3 on 2022-11-22 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=128, null=True)),
                ('mobile_number', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=128, null=True)),
                ('mobile_number', models.CharField(max_length=10, null=True)),
                ('specialities', models.CharField(blank=True, choices=[('Dermatologists', 'Dermatologists'), ('Cardiologists', 'Cardiologists'), ('Gastroenterologist', 'Gastroenterologist'), ('Physiotherapist', 'Physiotherapist'), ('Pharmacist', 'Pharmacist'), ('Orthopaedist', 'Orthopaedist'), ('Nephrologist', 'Nephrologist'), ('Neurologist', 'Neurologist'), ('Rectal Surgeons', 'Rectal Surgeons'), ('Anesthesiologists', 'Anesthesiologists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists')], max_length=255, null=True)),
                ('county', models.CharField(choices=[('Mombasa', 'Mombasa'), ('Nairobi', 'Nairobi')], max_length=255, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
