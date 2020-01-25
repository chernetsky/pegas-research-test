from django.urls import path
from . import views
from .views import (
    UserListView,
    UserDeleteView
)

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('create/', views.create, name='user-create'),
    path('<int:pk>/update/', views.update, name='user-update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete')
]
