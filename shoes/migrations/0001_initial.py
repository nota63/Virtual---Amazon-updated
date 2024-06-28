# Generated by Django 5.0.6 on 2024-06-25 07:19

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
                ('title', models.TextField()),
                ('price', tinymce.models.HTMLField()),
            ],
        ),
    ]
