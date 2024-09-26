from rest_framework import generics
from app.models import Post, Book
from app.serializers import PostSerializer, BooksSerializer
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.

class PostListView(generics.ListAPIView):
    model = Post
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['title', ]
    search_fields = ['title', ]
    ordering_fields = ['title', ]

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset


class PostDetailView(generics.RetrieveAPIView):
    model = Post
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset


class PostCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAdminUser]


class PostUpdateView(generics.UpdateAPIView):
    serializer_class = PostSerializer
    lookup_field = 'slug'
    model = Post

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset


class PostDeleteView(generics.DestroyAPIView):
    model = Post
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset


# For Book

class BookListView(generics.ListAPIView):
    model = Book
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['book_name', ]
    search_fields = ['book_name', ]
    ordering_fields = ['book_name', ]

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset


class BookDetailView(generics.RetrieveAPIView):
    model = Book
    serializer_class = BooksSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    model = Book
    # permission_classes = [IsAdminUser]


class BookUpdateView(generics.UpdateAPIView):
    serializer_class = BooksSerializer
    lookup_field = 'slug'
    model = Book

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset


class BookDeleteView(generics.DestroyAPIView):
    model = Book
    serializer_class = BooksSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset
