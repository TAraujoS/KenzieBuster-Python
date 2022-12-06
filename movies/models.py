from django.db import models

# Create your models here.


class MovieRating(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10)
    rating = models.CharField(
        max_length=20,
        choices=MovieRating.choices,
        default=MovieRating.G,
    )
    synopsis = models.TextField(null=True)

    user = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
