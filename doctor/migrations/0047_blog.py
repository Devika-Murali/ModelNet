# Generated by Django 4.2.5 on 2024-02-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0046_leaveapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('blog_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]