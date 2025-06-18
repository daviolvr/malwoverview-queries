from .views import HashView
from django.urls import path

urlpatterns = [
    path("insert-hash/", HashView.as_view(), name="insert-hash"),
]