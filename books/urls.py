from django.urls import path

from books.views import  BookListView, BookCreateView, BookDetailView

urlpatterns = [
    path("books/", BookListView.as_view(), name="books-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="books-detail"),
    path("books/create/", BookCreateView.as_view(), name="book-create")
]

app_name = "books"
