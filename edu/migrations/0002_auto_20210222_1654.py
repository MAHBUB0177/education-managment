# Generated by Django 3.1.6 on 2021-02-22 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academic_year',
            name='app_data_time',
        ),
        migrations.RemoveField(
            model_name='section_info',
            name='app_data_time',
        ),
    ]