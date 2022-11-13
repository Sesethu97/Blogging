# Generated by Django 4.0.6 on 2022-11-13 18:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startblog', '0024_alter_post_header_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='downvotes',
            new_name='dislike_counts',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='score',
            new_name='likes_counts',
        ),
        migrations.RemoveField(
            model_name='post',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.ManyToManyField(blank=True, default=None, related_name='dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
