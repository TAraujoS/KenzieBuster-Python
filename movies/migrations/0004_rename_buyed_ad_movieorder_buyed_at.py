# Generated by Django 4.1.4 on 2022-12-08 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_movieorder_movie_bought_by"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movieorder",
            old_name="buyed_ad",
            new_name="buyed_at",
        ),
    ]
