# Generated by Django 4.2.5 on 2023-09-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_remove_docprofile_licensenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='docprofile',
            name='add1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='add2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='fname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='lname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='postalcode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='services',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='specialist',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='docprofile',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
