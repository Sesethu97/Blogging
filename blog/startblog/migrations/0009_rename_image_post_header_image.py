# Generated by Django 4.0.6 on 2022-08-20 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startblog', '0008_merge_20220820_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='header_image',
        ),
    ]
