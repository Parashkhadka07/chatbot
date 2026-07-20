from django.urls import path
from .views import chat_bot

urlpatterns=[
    path("",chat_bot, name="chat_bot"),
]