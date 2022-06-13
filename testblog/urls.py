from django.urls import path
from .views import home
from .views import test

urlpatterns = [
    path('', home),
    path('test/', test),
]
