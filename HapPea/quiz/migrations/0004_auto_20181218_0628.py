# Generated by Django 2.0.5 on 2018-12-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_responseoption_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responseoption',
            name='time',
            field=models.FloatField(),
        ),
    ]
