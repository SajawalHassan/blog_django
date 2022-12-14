# Generated by Django 4.1 on 2022-08-28 13:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_alter_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='createdAt',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updatedAt',
            field=models.DateField(auto_now=True),
        ),
    ]
