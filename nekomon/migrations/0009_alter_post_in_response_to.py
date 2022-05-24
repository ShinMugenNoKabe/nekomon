# Generated by Django 4.0.4 on 2022-05-23 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nekomon', '0008_post_in_response_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='in_response_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='nekomon.post'),
        ),
    ]
