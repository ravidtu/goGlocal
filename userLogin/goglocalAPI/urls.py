from django.urls import path
from .views import ProfileList,UserViewSet
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls

urlpatterns = [
    path('login',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile', ProfileList.as_view()),
]
