# Generated by Django 4.0.6 on 2022-08-21 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startblog', '0009_rename_image_post_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]
