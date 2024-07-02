from django.urls import path

from .views import (
    LoginAPIView,
    LogoutAPIView,
    RefreshAPIView,
    ProtectedAPIView
)

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('refresh/', RefreshAPIView.as_view()),
    path('protected/', ProtectedAPIView.as_view())
]
