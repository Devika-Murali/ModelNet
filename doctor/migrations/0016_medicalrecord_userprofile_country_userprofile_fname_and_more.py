# Generated by Django 4.2.5 on 2023-10-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0015_userprofile_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis_date', models.DateField()),
                ('cancer_stage', models.CharField(max_length=255)),
                ('biopsy_results', models.TextField()),
                ('oncologist_name', models.CharField(max_length=255)),
                ('allergy_name', models.CharField(max_length=255)),
                ('allergy_severity', models.CharField(choices=[('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')], max_length=10)),
                ('medication_name', models.CharField(max_length=255)),
                ('dosage', models.CharField(max_length=50)),
                ('frequency', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='medical_history',
            field=models.FileField(blank=True, null=True, upload_to='medical_history/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
