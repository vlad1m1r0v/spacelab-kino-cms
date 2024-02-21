# Generated by Django 5.0.1 on 2024-02-17 21:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bannersettings',
            options={'verbose_name_plural': 'Banner Settings'},
        ),
        migrations.AddField(
            model_name='bannersettings',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bannersettings',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bannersettings',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]