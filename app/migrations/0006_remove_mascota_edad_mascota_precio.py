# Generated by Django 4.0.4 on 2022-06-24 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_mascota_imagenmascota'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='edad',
        ),
        migrations.AddField(
            model_name='mascota',
            name='precio',
            field=models.IntegerField(default=1, verbose_name='precio'),
            preserve_default=False,
        ),
    ]
