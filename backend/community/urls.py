from django.urls import path
from .views import SelectUser


urlpatterns = [
    path('select-user', SelectUser.as_view(), name="SelectUser")
]