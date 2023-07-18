from rest_framework import serializers
from .models import Gun


class GunSerializer(serializers.ModelSerializer):
    """
    Serializer for the Gun model
    Adds validation for the image
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    # Validation check using DRF field validation method
    # We use it to check size, format of the image
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image with width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image with height larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Gun
        fields = [
            'id', 'owner', 'brand', 'serial_number', 'created_at',
            'updated_at', 'gun_model', 'details', 'type', 'image',
            'is_owner',
        ]
