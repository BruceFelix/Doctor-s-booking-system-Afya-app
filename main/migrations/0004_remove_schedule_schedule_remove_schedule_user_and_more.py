# Generated by Django 4.1.3 on 2022-11-24 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_schedule_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='user',
        ),
        migrations.AddField(
            model_name='schedule',
            name='friday',
            field=models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='monday',
            field=models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='thursday',
            field=models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='tuesday',
            field=models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='wednesday',
            field=models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=255, null=True),
        ),
    ]