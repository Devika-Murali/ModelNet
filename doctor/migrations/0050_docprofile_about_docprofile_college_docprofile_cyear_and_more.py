# Generated by Django 4.2.5 on 2024-02-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0049_alter_blog_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='docprofile',
            name='about',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='college',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='cyear',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='degree',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]