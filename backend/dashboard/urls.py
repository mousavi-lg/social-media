from django.urls import path
from .views import MessageView, ProfileView

urlpatterns = [
    path('message', MessageView.as_view(), name="message"),
    path('profile', ProfileView.as_view(), name="profile")
]