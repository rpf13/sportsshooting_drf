from rest_framework import serializers
from .models import Usermessage


class UsermessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Usermessage model
    The currently logged in user will be used as the sender of
    the message
    """
    sender = serializers.ReadOnlyField(source='sender.username')
    is_sender = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='sender.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='sender.profile.image.url'
    )

    def get_is_sender(self, obj):
        request = self.context['request']
        return request.user == obj.sender

    class Meta:
        model = Usermessage
        fields = [
            'id', 'sender', 'is_sender', 'created_at', 'updated_at',
            'profile_id', 'profile_image', 'receiver', 'content',
        ]


class UsermessageDetailSerializer(UsermessageSerializer):
    """
    Serializer for the Usermessage model used in Detail view.
    Inherits from UsermessageSerializer.
    usermessage is a read only field so that we dont have to set
    this permission on each update
    """
    usermessage = serializers.ReadOnlyField(source='usermessage.id')
