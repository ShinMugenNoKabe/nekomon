# Generated by Django 4.0.4 on 2022-05-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nekomon', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=10),
        ),
    ]