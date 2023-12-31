# Generated by Django 3.2.20 on 2023-08-10 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mail',
            field=models.EmailField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_media',
            field=models.URLField(blank=True, max_length=50),
        ),
    ]
