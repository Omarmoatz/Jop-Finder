# Generated by Django 4.2.6 on 2024-01-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='company_logo')),
                ('about_us', models.TextField(max_length=300)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('fb_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('linkedIn_link', models.URLField()),
            ],
        ),
    ]
