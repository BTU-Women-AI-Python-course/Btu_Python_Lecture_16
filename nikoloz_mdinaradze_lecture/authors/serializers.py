from rest_framework import serializers

from authors.models import Author


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField(max_length=255)
    born_date = serializers.DateField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.born_date = validated_data.get('born_date', instance.born_date)
        instance.save()
        return instance
