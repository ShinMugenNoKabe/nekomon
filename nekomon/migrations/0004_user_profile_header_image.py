# Generated by Django 4.0 on 2021-12-25 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nekomon', '0003_alter_follow_user_followed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_header_image',
            field=models.CharField(default='nobg.png', max_length=200, verbose_name='Profile header image'),
            preserve_default=False,
        ),
    ]