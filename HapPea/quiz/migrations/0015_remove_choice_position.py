# Generated by Django 2.1.5 on 2019-04-07 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_news_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='position',
        ),
    ]