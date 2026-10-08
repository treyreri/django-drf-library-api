from django.urls import path

from .views import (  AuthorListCreateView,  BookListCreateView,  BookDetailView,  BookDeleteView, )


urlpatterns = [
    path('authors/', AuthorListCreateView.as_view()),
    path('books/', BookListCreateView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteView.as_view()),
]