# Generated by Django 4.2.5 on 2023-10-03 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0019_alter_patientinfo_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientinfo',
            name='patient',
        ),
    ]
