# Generated by Django 4.2.6 on 2023-10-31 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0005_alter_jop_options_jopform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jopform',
            name='cover_letter',
            field=models.TextField(help_text='add your notes here .....', max_length=600),
        ),
    ]
