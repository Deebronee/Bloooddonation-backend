# Generated by Django 3.2.9 on 2021-11-17 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20211117_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blood_donation_free_appointments',
            name='assigned',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='blood_donation_free_appointments',
            name='reserved',
            field=models.BooleanField(),
        ),
    ]
