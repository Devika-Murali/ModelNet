# Generated by Django 4.2.5 on 2024-02-09 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0052_referpatient'),
    ]

    operations = [
        migrations.AddField(
            model_name='referpatient',
            name='referring_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.docprofile'),
        ),
    ]
