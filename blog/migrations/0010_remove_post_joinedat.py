# Generated by Django 4.2.3 on 2023-08-03 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_joinedat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='joinedAt',
        ),
    ]
