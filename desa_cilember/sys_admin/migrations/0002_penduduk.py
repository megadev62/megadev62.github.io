# Generated by Django 3.1.7 on 2021-03-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Penduduk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=150, null=True)),
                ('nik', models.CharField(max_length=150, null=True)),
                ('tml', models.CharField(max_length=150, null=True)),
                ('ttl', models.DateField()),
                ('alamat', models.CharField(max_length=150, null=True)),
                ('rtrw', models.CharField(max_length=150, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
