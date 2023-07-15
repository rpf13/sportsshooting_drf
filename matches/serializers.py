from rest_framework import serializers
from matches.models import Match


class MatchSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

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
        model = Match
        fields = [
            'id', 'owner', 'title', 'created_at', 'updated_at',
            'match_date', 'match_location', 'division', 'details',
            'image', 'level_filter', 'is_owner', 'profile_id',
            'profile_image',
        ]
