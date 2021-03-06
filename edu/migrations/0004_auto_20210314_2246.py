# Generated by Django 3.1.6 on 2021-03-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0003_academic_year_app_data_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result_Grade',
            fields=[
                ('grade_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('grade_name', models.CharField(max_length=20)),
                ('result_gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=22, null=True)),
                ('lowest_mark', models.DecimalField(blank=True, decimal_places=2, max_digits=22, null=True)),
                ('highest_mark', models.DecimalField(blank=True, decimal_places=2, max_digits=22, null=True)),
                ('is_failed', models.BooleanField(blank=True, default=False)),
                ('app_user_id', models.CharField(blank=True, max_length=20)),
                ('app_data_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='occupation_info',
            name='app_data_time',
        ),
        migrations.RemoveField(
            model_name='students_info',
            name='academic_year',
        ),
        migrations.DeleteModel(
            name='Academic_Year',
        ),
    ]
