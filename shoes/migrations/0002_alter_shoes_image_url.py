# Generated by Django 5.0.6 on 2024-06-25 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='image_url',
            field=models.CharField(max_length=5000),
        ),
    ]