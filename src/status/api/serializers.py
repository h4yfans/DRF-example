from rest_framework import serializers
from status.models import Status


# class CustomSerializer(serializers.Serializer):
#     content = serializers.CharField()
#     email = serializers.EmailField()
#

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError('This is way too long.')
    #     return value

    def validate(self, attrs):
        content = attrs.get('content', None)
        if content == '':
            content = None
        image = attrs.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError('Content or Image is required')
        return attrs
