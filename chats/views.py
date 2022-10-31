from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import Chat, Inbox
from .serializers import ChatSerializer
from .serializers import ChatSerializer, InboxSerializer

User = get_user_model()

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


class InboxChatAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self, request, inbox_id):
        inbox = Inbox.objects.get(pk=inbox_id)
        chats = Chat.objects.filter(inbox=inbox)
        serializer = ChatSerializer(chats, many=True)
        return Response ({"message": serializer.data}, status=status.HTTP_200_OK)


class AllInboxAPIView(APIView):        
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self, request):
        all_inbox = Inbox.objects.filter(sender=request.user, receiver=request.user)
        serializer = InboxSerializer(all_inbox, many=True)
        return Response ({"message": serializer.data}, status=status.HTTP_200_OK)


