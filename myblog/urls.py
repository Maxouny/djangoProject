from django.urls import path
from myblog.views import home
from myblog.views import test

urlpatterns = [
    path('', home),
    path('test/', test),
]
