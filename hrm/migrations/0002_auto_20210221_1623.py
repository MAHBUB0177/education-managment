# Generated by Django 3.1.5 on 2021-02-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift_info',
            name='office_id',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]