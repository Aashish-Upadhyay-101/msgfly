from django.contrib import admin
from .models import Chat, Inbox


class InboxAdmin(admin.ModelAdmin):
    list_display = ["pk", "sender", "receiver"]

admin.site.register(Chat)
admin.site.register(Inbox, InboxAdmin)

