# Generated by Django 4.2.5 on 2024-02-19 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0060_appointments_delete_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointments',
            old_name='patient',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='appointments',
            old_name='reason_for_consultation',
            new_name='reason',
        ),
    ]
