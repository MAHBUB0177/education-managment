# Generated by Django 3.1.6 on 2021-03-18 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0027_remove_academic_class_subject_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='academic_class',
            name='subject_list',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]