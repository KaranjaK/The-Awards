# Generated by Django 3.2.10 on 2022-04-11 08:19

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_awards', '0002_alter_projects_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('bio', models.CharField(max_length=40)),
                ('projects', models.CharField(max_length=60)),
                ('contact', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='projects',
            name='ratings',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='projects',
            name='reviews',
            field=models.CharField(default='0', max_length=150),
        ),
    ]
