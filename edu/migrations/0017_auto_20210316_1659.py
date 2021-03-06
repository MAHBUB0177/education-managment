# Generated by Django 3.1.6 on 2021-03-16 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0016_remove_students_info_exam_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_marks_details',
            name='student_roll',
            field=models.ForeignKey(blank=True, db_column='student_roll', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emd_student_roll', to='edu.students_info'),
        ),
        migrations.AlterField(
            model_name='student_admission',
            name='student_roll',
            field=models.ForeignKey(blank=True, db_column='student_roll', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sta_student_roll', to='edu.students_info'),
        ),
    ]
