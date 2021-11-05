# Generated by Django 3.1.6 on 2021-03-18 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0028_academic_class_subject_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject_list',
            name='class_group_id',
            field=models.ForeignKey(blank=True, db_column='class_group_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cgp_class_id3', to='edu.academic_class_group'),
        ),
        migrations.AddField(
            model_name='subject_list',
            name='class_id',
            field=models.ForeignKey(blank=True, db_column='class_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cgp_class_id1', to='edu.academic_class'),
        ),
    ]
