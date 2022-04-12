# Generated by Django 3.2.10 on 2022-04-12 02:07

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('link', models.CharField(max_length=40)),
                ('date', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('design', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('usability', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('content', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('score', models.FloatField(blank=True, default=0)),
                ('design_average', models.FloatField(blank=True, default=0)),
                ('usability_average', models.FloatField(blank=True, default=0)),
                ('content_average', models.FloatField(blank=True, default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rater', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='the_awards.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('bio', models.CharField(max_length=40)),
                ('projects', models.CharField(max_length=60)),
                ('contact', models.EmailField(blank=True, max_length=150)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
