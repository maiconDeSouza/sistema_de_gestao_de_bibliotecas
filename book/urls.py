from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListBooks.as_view(), name='index'),
    path('<int:pk>/<str:status>/', views.ChangeStatus.as_view(), name='status')
]
