# Generated by Django 3.2.20 on 2023-07-15 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
