# Generated by Django 4.2.5 on 2024-02-01 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0047_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='image',
            new_name='images',
        ),
    ]
