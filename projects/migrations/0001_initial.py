# Generated by Django 4.0.2 on 2022-04-07 20:52

from django.db import migrations, models
import markdownfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('overview', models.TextField()),
                ('description', markdownfield.models.MarkdownField(rendered_field='text_rendered', use_editor=False)),
                ('text_rendered', markdownfield.models.RenderedMarkdownField()),
                ('image', models.ImageField(upload_to='projects/static/projects/images/')),
            ],
        ),
    ]
