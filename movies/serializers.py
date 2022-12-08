from rest_framework import serializers
from movies.models import Movie, MovieRating, MovieOrder
import ipdb


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    synopsis = serializers.CharField(allow_null=True, default=None)
    duration = serializers.CharField(allow_null=True, default=None, max_length=10)
    rating = serializers.ChoiceField(
        choices=MovieRating.choices,
        default=MovieRating.G,
    )

    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):
        return obj.user.email

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = serializers.DateTimeField(read_only=True)
    title = serializers.SerializerMethodField()
    buyed_by = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.movie.title

    def get_buyed_by(self, obj):
        return obj.user.email

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
