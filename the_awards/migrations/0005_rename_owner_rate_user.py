# Generated by Django 3.2.10 on 2022-04-12 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_awards', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='owner',
            new_name='user',
        ),
    ]