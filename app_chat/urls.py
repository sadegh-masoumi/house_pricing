from django.urls import path
from .views import Chat, Send


urlpatterns = [
    path('chat/', Chat.as_view(), name='chat_all'),
    path('chat/<recipient>', Chat.as_view(), name='chat'),
    path('send/', Send.as_view(), name='send')
]
