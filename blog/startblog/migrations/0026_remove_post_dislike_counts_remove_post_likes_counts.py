# Generated by Django 4.0.6 on 2022-11-13 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startblog', '0025_rename_downvotes_post_dislike_counts_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislike_counts',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes_counts',
        ),
    ]
