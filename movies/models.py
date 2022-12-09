from django.db import models


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

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )

    bought_by = models.ManyToManyField(
        "users.User",
        through="movies.MovieOrder",
        related_name="bought_movies",
    )

    def __repr__(self) -> str:
        return f"<[{self.id}] - {self.title}>"


class MovieOrder(models.Model):
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movie_order",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movie_buyer",
    )
    buyed_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
