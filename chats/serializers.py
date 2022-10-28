from rest_framework import serializers
from .models import Chat, Inbox
from users.serializers import UserSerializer


class InboxSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Inbox
        fields = "__all__"


class ChatSerializer(serializers.ModelSerializer):
    inbox = InboxSerializer()

    class Meta:
        model = Chat 
        fields = "__all__"

