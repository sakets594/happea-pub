# Generated by Django 2.1.5 on 2019-04-06 19:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_auto_20190406_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
