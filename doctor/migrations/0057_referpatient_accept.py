# Generated by Django 4.2.5 on 2024-02-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0056_alter_referpatient_case_sheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='referpatient',
            name='accept',
            field=models.BooleanField(default=False),
        ),
    ]
