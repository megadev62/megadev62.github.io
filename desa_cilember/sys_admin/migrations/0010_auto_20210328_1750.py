# Generated by Django 3.1.7 on 2021-03-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_admin', '0009_auto_20210328_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
