# Generated by Django 2.0.5 on 2018-12-18 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_responseoption_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='responseoption',
            name='choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Choice'),
        ),
    ]
