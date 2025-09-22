from django.urls import path
from .views.view import post_hello

urlpatterns = [
    path('hello/', post_hello, name='post_hello'),
]
