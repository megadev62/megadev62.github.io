# Generated by Django 3.1.7 on 2021-03-28 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_admin', '0010_auto_20210328_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255, null=True)),
                ('slug', models.SlugField(max_length=255)),
                ('img1', models.ImageField(blank=True, null=True, upload_to='gambar_berita/')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='gambar_berita/')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='gambar_berita/')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='gambar_berita/')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='gambar_berita/')),
                ('img6', models.ImageField(blank=True, null=True, upload_to='gambar_berita/')),
                ('img7', models.ImageField(blank=True, null=True, upload_to='gambar_berita/')),
                ('img8', models.ImageField(blank=True, null=True, upload_to='gambar_berita/')),
                ('img9', models.ImageField(blank=True, null=True, upload_to='gambar_berita/')),
                ('img10', models.ImageField(blank=True, null=True, upload_to='gambar_berita/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
