# Generated by Django 4.0.6 on 2022-08-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startblog', '0011_alter_post_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
