# Generated by Django 4.2.3 on 2023-08-03 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_post_joinedat'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default='default.jpg', upload_to='post_files'),
        ),
    ]
