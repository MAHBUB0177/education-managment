# Generated by Django 3.1.6 on 2021-03-18 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0019_student_admission_add_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam_setup',
            name='examtype_id',
        ),
        migrations.DeleteModel(
            name='Exam_Marks_Details',
        ),
        migrations.DeleteModel(
            name='Exam_Setup',
        ),
    ]
