# Generated by Django 3.0.6 on 2020-05-23 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_artist_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='artist',
            new_name='song_name',
        ),
    ]
