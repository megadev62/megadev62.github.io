# Generated by Django 3.1.7 on 2021-03-27 18:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sys_admin', '0003_auto_20210328_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='aparatur',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
