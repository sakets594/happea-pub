# Generated by Django 2.1.5 on 2019-01-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='category',
            field=models.ManyToManyField(to='quiz.Category', verbose_name='category'),
        ),
    ]
