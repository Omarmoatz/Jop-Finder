# Generated by Django 4.2.6 on 2024-01-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_qoute_alter_blog_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='auther_img')),
            ],
        ),
    ]
