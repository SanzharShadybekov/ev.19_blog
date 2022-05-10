from ast import Return
from django import views
from rest_auth.views import LogoutView
from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from blog_api import serializers
from blog_api.models import Post, Category
from blog_api.permissions import IsAuthor

# TODO permissions to post and comments
# TODO end comments CRUD
# TODO Add Likes

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.RegisterSerializer


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated, )


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer


# class PostCreateView(generics.CreateAPIView):
#     serializer_class = serializers.PostSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class PostListView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer

# class PostDetailView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer

# class PostUpdateView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer

# class PostDeleteView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer

class PostViewSet(ModelViewSet):
    class Meta:
        model = Post
        fields = '__all__'
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('category', 'owner')
    search_fields = ('title',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_permissions(self):
        #Создавать посты может залогиненный пользователь
        if self.action in ('create',):
            return [permissions.IsAuthenticated(),]
        # изменять и удалять может только автор
        elif self.action in ('update', 'partial_update','destroy',):
            return [IsAuthor(),]
        # просматривать могут все
        else:
            return [permissions.AllowAny(),]






# class PostView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True,)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = PostSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)


# class PostDetailView(APIView):
#     @staticmethod
#     def get_object(pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Exception("Not found")
    
#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors)
    
#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response("Deleted", status=204)
    

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
