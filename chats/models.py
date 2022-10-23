from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth import get_user_model


User = get_user_model()


class Chat(models.Model):
    message_from = models.ForeignKey(User, related_name="chat_from", on_delete=models.CASCADE)
    message_to = models.ForeignKey(User, related_name="chat_to", on_delete=models.CASCADE)
    message = models.TextField(verbose_name=_("Message"), max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Chat")
        verbose_name_plural = _("Chats")

    def __str__(self):
        return self.name

