# fibonacci_api/urls.py
from django.urls import path
from fibonacci.views import fibonacci

urlpatterns = [
    path('fib', fibonacci, name='fibonacci'),
]
