# Generated by Django 4.1 on 2022-08-28 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_post_createdat_post_updatedat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-createdAt', '-updatedAt']},
        ),
    ]
