# Generated by Django 3.1.6 on 2021-03-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appauth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_settings',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_settings',
            name='app_user_id',
            field=models.CharField(blank=True, max_length=20, primary_key=True, serialize=False),
        ),
    ]
