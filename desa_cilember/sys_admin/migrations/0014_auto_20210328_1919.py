# Generated by Django 3.1.7 on 2021-03-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_admin', '0013_auto_20210328_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparatur',
            name='slug',
            field=models.SlugField(max_length=150, null=True),
        ),
    ]
