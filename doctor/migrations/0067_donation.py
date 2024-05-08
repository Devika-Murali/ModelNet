# Generated by Django 4.2.5 on 2024-02-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0066_alter_leaverequest_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('place', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]