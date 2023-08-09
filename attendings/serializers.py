from django.db import IntegrityError
from rest_framework import serializers
from .models import Attending


class AttendingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    class Meta:
        model = Attending
        fields = [
            'id',
            'created_at',
            'owner',
            'profile_id',
            'profile_image',
            'match',
        ]

    # Validate that a user cannot attend a match twice
    # done via using integrity error
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate,'
                'youn cannot attend a match twice!'
            })
