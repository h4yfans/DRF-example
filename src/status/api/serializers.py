from rest_framework import serializers
from status.models import Status

from accounts.api.serializers import UserPublicSerializer


# class CustomSerializer(serializers.Serializer):
#     content = serializers.CharField()
#     email = serializers.EmailField()
#
class StatusInlineUserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Status
        fields = [
            'id',
            'content',
            'image',
            'uri'
        ]

    def get_uri(self, obj):
        return f'api/status/{obj.id}'


class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
            'uri'
        ]
        read_only_fields = ['user']  # GET #readyonly_fields

    def get_uri(self, obj):
        return f'api/status/{obj.id}'

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
