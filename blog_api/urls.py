from django.urls import path, include

from blog_api import views

urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),
    path('users/register/', views.UserRegistrationView.as_view()),
    path('users/logout/', views.CustomLogoutView.as_view()),
    path('users/rest_auth/', include('rest_auth.urls')),
]
