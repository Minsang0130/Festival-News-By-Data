# Generated by Django 4.2.16 on 2024-11-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivals_details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival_details',
            name='Main_Region',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='지역권'),
        ),
    ]
