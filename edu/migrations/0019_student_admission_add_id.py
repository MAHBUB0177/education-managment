# Generated by Django 3.1.6 on 2021-03-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0018_remove_student_admission_add_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_admission',
            name='add_id',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]