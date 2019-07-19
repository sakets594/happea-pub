# Generated by Django 2.0.5 on 2018-12-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='agegroup',
            field=models.IntegerField(choices=[(0, 'none'), (1, '10-18 yrs'), (2, '19-25 yrs'), (3, '26-40 yrs'), (4, '40+ yrs')], default=1),
        ),
    ]
