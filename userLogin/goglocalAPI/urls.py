from django.urls import path
from .views import UserList,ProfileList

urlpatterns = [
    path('login', UserList.as_view()),
    path('profile', ProfileList.as_view()),
]
