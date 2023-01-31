# Generated by Django 4.1.4 on 2023-01-31 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Movies", "0003_movies_active"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movies",
            name="category",
        ),
        migrations.AddField(
            model_name="movies",
            name="category",
            field=models.ManyToManyField(to="Movies.categories"),
        ),
    ]
