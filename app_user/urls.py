from django.urls import path
from .views import Login, Register, Logout, Dashboard


urlpatterns = [
    path('accounts/login/', Login.as_view(), name='login'),
    path('accounts/register/', Register.as_view(), name='register'),
    path('accounts/logout/', Logout.as_view(), name='logout'),
    path('accounts/dashboard/', Dashboard.as_view(), name='dashboard'),
]
