# Generated by Django 4.2.5 on 2023-10-11 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0038_alter_appointment_age_alter_appointment_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='docprofile',
            name='booked_time_slots',
            field=models.JSONField(default=dict),
        ),
    ]
