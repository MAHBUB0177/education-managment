# Generated by Django 3.1.6 on 2021-03-15 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0005_academic_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_Type',
            fields=[
                ('examtype_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('examtype_name', models.CharField(max_length=20)),
                ('app_user_id', models.CharField(blank=True, max_length=20)),
                ('app_data_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
