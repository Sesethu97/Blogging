# Generated by Django 4.0.6 on 2022-08-14 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startblog', '0011_profile_facebook_url_profile_instagram_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
    ]