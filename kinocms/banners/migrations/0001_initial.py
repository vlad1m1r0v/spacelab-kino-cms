# Generated by Django 5.0.1 on 2024-02-17 19:47

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementBanner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BannerSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_rotation', models.PositiveSmallIntegerField()),
                ('advertisement_rotation', models.PositiveSmallIntegerField()),
                ('background_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('is_background_image', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TopBanner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('url', models.URLField()),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
