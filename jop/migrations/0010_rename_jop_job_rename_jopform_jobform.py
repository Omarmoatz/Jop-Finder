# Generated by Django 4.2.6 on 2024-01-05 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0009_alter_jopform_cv'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jop',
            new_name='Job',
        ),
        migrations.RenameModel(
            old_name='JopForm',
            new_name='JobForm',
        ),
    ]
