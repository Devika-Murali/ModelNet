# Generated by Django 4.2.5 on 2023-10-20 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0044_remove_appointment_date_appointment_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=50, null=True),
        ),
    ]