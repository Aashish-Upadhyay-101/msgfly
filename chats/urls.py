from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("all/", views.AllChatAPIView.as_view(), name="all_chats"),
    path("<str:room_name>/", views.room, name="room"),
]
