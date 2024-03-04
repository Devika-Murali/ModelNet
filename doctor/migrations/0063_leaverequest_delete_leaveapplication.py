# Generated by Django 4.2.5 on 2024-02-23 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0062_docprofile_from_date_docprofile_hospital_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('sick', 'Sick Leave'), ('casual', 'Casual Leave'), ('emergency', 'Emergency Leave')], max_length=20)),
                ('num_days', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('leave_reason', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='LeaveApplication',
        ),
    ]
