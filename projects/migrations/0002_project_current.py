# Generated by Django 4.0.2 on 2022-04-07 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='current',
            field=models.BooleanField(default=True),
        ),
    ]