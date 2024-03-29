# Generated by Django 4.2.5 on 2024-02-23 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0063_leaverequest_delete_leaveapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='doctor_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='leave_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='num_days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
