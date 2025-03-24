from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.CreateAuthor.as_view(), name='newauthor'),
]
