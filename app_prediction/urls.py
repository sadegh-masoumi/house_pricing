from django.urls import path
from .views import Prediction


urlpatterns = [
    path('prediction/', Prediction.as_view(), name='prediction'),
]
