
from django.urls import path
from . import views

urlpatterns = [
    # for Post
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post-detail/<slug:slug>/', views.PostDetailView.as_view(), name='post'),
    path('add-post/', views.PostCreateView.as_view(), name='add-post'),
    path('post-update/<slug:slug>/', views.PostUpdateView.as_view(), name='post-update'),
    path('delete-post/<slug:slug>/', views.PostDeleteView.as_view(), name='delete-post'),

    # for Book
    path('books/', views.BookListView.as_view(), name='books'),
    path('book-detail/<slug:slug>/', views.BookDetailView.as_view(), name='book'),
    path('add-book/', views.BookCreateView.as_view(), name='add-book'),
    path('book-update/<slug:slug>/', views.BookUpdateView.as_view(), name='book-update'),
    path('delete-book/<slug:slug>/', views.BookDeleteView.as_view(), name='book-delete'),




]
