# Generated by Django 2.1.5 on 2019-04-07 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0017_auto_20190407_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(upload_to='news/'),
        ),
    ]
