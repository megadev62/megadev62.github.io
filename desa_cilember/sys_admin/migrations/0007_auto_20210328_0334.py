# Generated by Django 3.1.7 on 2021-03-27 20:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sys_admin', '0006_auto_20210328_0259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='penduduk',
            options={'ordering': ['-update']},
        ),
        migrations.AddField(
            model_name='penduduk',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
