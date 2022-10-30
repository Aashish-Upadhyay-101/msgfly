import uuid 
from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth import get_user_model


User = get_user_model()


class Inbox(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sender.id}-{self.receiver.id}"


class Chat(models.Model):
    inbox = models.ForeignKey(Inbox, related_name="chat", on_delete=models.CASCADE)
    message = models.TextField(verbose_name=_("Message"), max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Chat")
        verbose_name_plural = _("Chats")

    def __str__(self):
        return self.message




