# Generated by Django 4.2.5 on 2023-10-05 09:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_otdels_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='otdels',
            name='kod',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
