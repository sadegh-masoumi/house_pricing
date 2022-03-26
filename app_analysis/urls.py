from django.urls import path
from .views import Analysis


urlpatterns = [
    path('analysis/', Analysis.as_view(), name='analysis'),
]
