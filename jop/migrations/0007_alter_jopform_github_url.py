# Generated by Django 4.2.6 on 2023-11-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0006_alter_jopform_cover_letter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jopform',
            name='github_url',
            field=models.URLField(blank=True, help_text='please enter your github account', null=True),
        ),
    ]
