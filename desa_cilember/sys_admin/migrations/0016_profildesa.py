# Generated by Django 3.1.7 on 2021-03-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_admin', '0015_auto_20210328_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilDesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=150, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('tlp', models.CharField(max_length=13, null=True)),
                ('wa', models.CharField(max_length=13, null=True)),
                ('alamat', models.CharField(max_length=150, null=True)),
                ('kab', models.CharField(max_length=150, null=True)),
                ('prov', models.CharField(max_length=150, null=True)),
                ('pos', models.CharField(max_length=7, null=True)),
                ('visi', models.TextField()),
                ('misi', models.TextField()),
                ('kades', models.TextField()),
            ],
        ),
    ]
