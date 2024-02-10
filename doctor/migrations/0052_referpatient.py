# Generated by Django 4.2.5 on 2024-02-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0051_alter_docprofile_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=100)),
                ('patient_name', models.CharField(max_length=100)),
                ('medical_details', models.FileField(upload_to='medical_details/%Y/%m/%d/')),
                ('referred_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]