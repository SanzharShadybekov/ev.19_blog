from django.urls import path

from blog_api import views

urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('users/register/', views.UserRegistrationView.as_view()),
]
