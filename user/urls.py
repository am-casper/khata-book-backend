from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserDetailView.as_view(), name='user-detail'),
    path('create', views.UserCreateView.as_view(), name='user-create'),
]