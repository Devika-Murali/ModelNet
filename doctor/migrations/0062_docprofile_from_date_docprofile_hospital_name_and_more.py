# Generated by Django 4.2.5 on 2024-02-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0061_rename_patient_appointments_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='docprofile',
            name='from_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='hospital_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='to_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
