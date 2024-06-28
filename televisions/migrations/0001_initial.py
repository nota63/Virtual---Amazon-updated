# Generated by Django 5.0.6 on 2024-06-25 10:42

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Televisions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField()),
                ('title', models.TextField()),
                ('price', tinymce.models.HTMLField()),
            ],
        ),
    ]