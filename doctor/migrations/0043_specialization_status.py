# Generated by Django 4.2.5 on 2023-10-20 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0042_alter_payment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]