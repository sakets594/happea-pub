# Generated by Django 2.0.5 on 2018-12-19 17:51

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20181212_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contactnu',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True),
        ),
    ]