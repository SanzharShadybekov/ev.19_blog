from django.contrib import admin

from blog_api.models import Category, Post

admin.site.register(Post)
admin.site.register(Category)
