from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('blog_api.urls')),
]
# /post/ CreateAPiVIEW
#
# localhost:8000/api/v1/post/