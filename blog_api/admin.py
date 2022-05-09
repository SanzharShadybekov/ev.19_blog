from django.contrib import admin

from blog_api.models import Category, Post, PostImages

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostImages)
