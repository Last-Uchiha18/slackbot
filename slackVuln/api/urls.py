from django.urls import path
from .views import button_clicked

urlpatterns = [
    path('slack/interactive/', button_clicked)
]