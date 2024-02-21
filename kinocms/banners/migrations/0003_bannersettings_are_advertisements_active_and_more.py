# Generated by Django 5.0.1 on 2024-02-18 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0002_alter_bannersettings_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannersettings',
            name='are_advertisements_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bannersettings',
            name='are_banners_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bannersettings',
            name='advertisement_rotation',
            field=models.PositiveSmallIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='bannersettings',
            name='banner_rotation',
            field=models.PositiveSmallIntegerField(default=5),
        ),
    ]