from rest_framework import serializers
from .models import Usermessage


class UsermessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Usermessage model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Usermessage
        fields = [
            'id', 'owner', 'is_owner', 'created_at', 'updated_at',
            'profile_id', 'profile_image', 'sender', 'receiver',
            'content',
        ]


class UsermessageDetailSerializer(UsermessageSerializer):
    """
    Serializer for the Usermessage model used in Detail view.
    Inherits from UsermessageSerializer.
    usermessage is a read only field so that we dont have to set
    this permission on each update
    """
    usermessage = serializers.ReadOnlyField(source='usermessage.id')
