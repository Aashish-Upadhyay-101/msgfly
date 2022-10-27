import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .exceptions import LoginRequiredException
from users.models import User
from .models import Inbox, Chat


class ChatConsumer(AsyncWebsocketConsumer):
    # connect to a group/inbox that user whats to communicate to
    async def connect(self):
        # get current logged in user
        user = self.scope["user"]
        if user.is_anonymous:
            raise LoginRequiredException

        # sender and receiver's id from url_route of channels
        self.sender_id = user.id
        self.receiver_id = self.scope["url_route"]["kwargs"]["receiver_id"]

        self.sender_user = await database_sync_to_async(self.get_user)(self.sender_id)
        self.receiver_user = await database_sync_to_async(self.get_user)(self.receiver_id)

        # get or create inbox
        inbox, created = await database_sync_to_async(self.create_inbox)()
        self.inbox = inbox 

        # channel room group name
        self.room_group_name = f"{self.sender_id}-{self.receiver_id}"
        
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()


    def get_user(self, id):
        return User.objects.get(id=id)


    def create_inbox(self):
        return Inbox.objects.get_or_create(sender=self.sender_user, receiver=self.receiver_user)

    
    def get_all_messages(self):
        return Chat.objects.filter(inbox=self.inbox).order_by("created_at")


    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)


    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group 
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )


    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))


            