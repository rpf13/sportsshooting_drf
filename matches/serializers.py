from rest_framework import serializers
from .models import Match
from attendings.models import Attending


class MatchSerializer(serializers.ModelSerializer):
    """
    Serializer for the Match model
    Adds validation for the image
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    attending_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    attendings_count = serializers.ReadOnlyField()
    match_date = serializers.DateField(
        format="%d %b %Y", input_formats=['%d %b %Y', 'iso-8601']
    )

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

    # if user is logged in and authenticated
    # filter attending objects to see if user is
    # attending match and if so, set attending
    # variable. If this variable is set, return the
    # attending_id, else None
    def get_attending_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            attending = Attending.objects.filter(
                owner=user, match=obj
            ).first()
            return attending.id if attending else None
        return None

    class Meta:
        model = Match
        fields = [
            'id', 'owner', 'title', 'created_at', 'updated_at',
            'match_location', 'match_date', 'level_filter', 'division',
            'details', 'image', 'is_owner', 'profile_id',
            'profile_image', 'attending_id', 'comments_count',
            'attendings_count',
        ]
