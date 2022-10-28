from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Chat, Inbox
from .serializers import ChatSerializer

# template
def index(request):
    return render(request, "chats/index.html")

def room(request, room_name):
    return render (request, "chats/room.html", {"room_name": room_name})


# rest api 
class AllChatAPIView(ListAPIView):
    queryset = Chat.objects.all().order_by("created_at")
    serializer_class = ChatSerializer
    lookup_field = 'id'
    