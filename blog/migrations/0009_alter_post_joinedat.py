# Generated by Django 4.2.3 on 2023-08-03 08:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_joinedat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='joinedAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]