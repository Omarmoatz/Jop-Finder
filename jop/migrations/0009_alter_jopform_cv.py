# Generated by Django 4.2.6 on 2023-11-02 11:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0008_alter_jopform_jop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jopform',
            name='cv',
            field=models.FileField(help_text='please uplouad your CV', upload_to='cv', validators=[django.core.validators.FileExtensionValidator(['pdf'], 'Only PDF files are allowed.')]),
        ),
    ]
