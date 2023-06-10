from rest_framework import serializers
from portofolio.models import  Tag, StarTest,Category

class StarTestSerializer(serializers.Serializer):
    title = serializers.CharField()
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name'
    )
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        slug_field='caption'
    )

    def create(self, validated_data): 
        tags = validated_data.pop('tags')
        startest = StarTest.objects.create(**validated_data)

        for tag in tags:
            tagy = Tag.objects.get(caption=tag)
            startest.tags.add(tagy)
        
        return startest
