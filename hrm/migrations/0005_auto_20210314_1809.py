# Generated by Django 3.1.5 on 2021-03-14 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0004_auto_20210226_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave_application',
            name='application_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='leave_application',
            name='approval_status',
            field=models.CharField(blank=True, default='Panding', max_length=10, null=True),
        ),
    ]
