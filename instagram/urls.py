from django.urls import path
from .views import StoryAPIView, ProfileAPIView

urlpatterns = [
    path('profiles', ProfileAPIView.as_view()),
    path('stories', StoryAPIView.as_view())
]
