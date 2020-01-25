from django.urls import path
from . import views
from .views import UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('create/', views.create, name='user-create'),
    path('<int:pk>/update/', views.update, name='user-update')
]
