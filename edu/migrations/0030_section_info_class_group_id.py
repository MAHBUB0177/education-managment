# Generated by Django 3.1.6 on 2021-03-18 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0029_auto_20210318_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='section_info',
            name='class_group_id',
            field=models.ForeignKey(db_column='class_group_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sec_class_group_id', to='edu.academic_class_group'),
        ),
    ]