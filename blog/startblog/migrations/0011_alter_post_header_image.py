# Generated by Django 4.0.6 on 2022-08-21 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startblog', '0010_alter_post_header_image_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/post'),
        ),
    ]
