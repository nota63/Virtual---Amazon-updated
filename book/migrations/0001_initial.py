# Generated by Django 5.0.6 on 2024-06-24 13:33

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=1000)),
                ('title', tinymce.models.HTMLField()),
                ('price', models.TextField()),
            ],
        ),
    ]