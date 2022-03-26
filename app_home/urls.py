from django.urls import path
from .views import Home, SendEmail


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('email', SendEmail.as_view(), name='send_email'),
]
