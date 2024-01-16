from django.http import HttpResponse
from django.urls import path

from front.views import MainIndexView

urlpatterns = [
    path('', MainIndexView.as_view(), name='home')
]