from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListBooks.as_view(), name='index'),
    path('/', views.CreateNewbook.as_view(), name='new'),
    path('<int:pk>/<str:status>/', views.ChangeStatus.as_view(), name='status'),
    path('filter/', views.FilterBooks.as_view(), name='filter'),
    path('search/', views.SearchBooks.as_view(), name='search'),
]
