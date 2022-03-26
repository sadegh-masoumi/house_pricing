from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message
from collections import defaultdict
from django.db.models import Q
from app_user.models import User


class Chat(LoginRequiredMixin, View):
    def get(self, request, recipient='all'):
        messages = Message.objects.filter(
            Q(sender=request.user) | Q(recipient=request.user))

        grouped_message = defaultdict(list)
        for msg in messages:
            if msg.sender != request.user:
                grouped_message[msg.sender.email].append(msg)
            elif msg.recipient != request.user:
                grouped_message[msg.recipient.email].append(msg)

        grouped_message_list = [(group, sorted(message, key=lambda item: item.time))
                                for group, message in grouped_message.items()]
        grouped_message_list.sort(key=lambda item: item[1][-1].time)

        chat = []
        if recipient != 'all':
            given_user = User.objects.filter(email=recipient)
            if given_user.exists():
                current_chat = Message.objects.filter(Q(sender=given_user[0]) | Q(recipient=given_user[0]))
                if len(current_chat) > 0:
                    chat.append((
                        given_user[0].email,
                        sorted(current_chat, key=lambda item: item.time)
                    ))

        while True:
            if len(chat) == 5 or len(grouped_message_list) == 0:
                break
            if grouped_message_list[-1][0] != recipient:
                chat.append((
                    grouped_message_list[-1][0],
                    grouped_message_list[-1][1]
                ))
            grouped_message_list.pop()

        chat = [(User.objects.get(email=email), message) for email, message in chat]
        return render(request, 'chat.html', {
            'chat': chat,
            'last': chat[0][1][-1] if len(chat[0]) > 1 and len(chat[0][1]) > 1 else []
        })


class Send(LoginRequiredMixin, View):
    def post(self, request):
        sender = request.user
        recipient_email = request.POST.get('recipient')
        recipient = User.objects.get(email=recipient_email)
        text = request.POST.get('text')
        Message.objects.create(
            sender=sender,
            recipient=recipient,
            text=text
        )
        return redirect(reverse('chat', kwargs={'recipient': recipient_email}))
