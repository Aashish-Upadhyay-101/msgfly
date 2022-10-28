# Generated by Django 4.1.2 on 2022-10-27 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0002_inbox'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='message_from',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='message_to',
        ),
        migrations.AddField(
            model_name='chat',
            name='inbox',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='chat', to='chats.inbox'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inbox',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inbox',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]