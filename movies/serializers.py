from rest_framework import serializers


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    synopsis = serializers.CharField()
    duration = serializers.CharField(max_length=10)
    rating = serializers.CharField(max_length=20)
    # added_by = (many=True)

    def create(self, validated_data):
        ...

    def update(self, instance, validated_data):
        ...
