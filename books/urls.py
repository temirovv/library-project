from django.urls import path
from .views import (
    BookCreateApi, BookDetailApi, 
    BookUpdateApi, BookDeleteApi, 
    BookListCreateApi, BookUpdateDeleteApi, BookListApi)


urlpatterns = [
    # path('', BookListCreateApi.as_view(), name='home'),
    path("", BookListApi.as_view()),
    path('book/create/', BookCreateApi.as_view()),
    path('book/update/<int:pk>/', BookUpdateDeleteApi.as_view()),
    path('<int:pk>/', BookDetailApi.as_view()),
    path('<int:pk>/update/', BookUpdateApi.as_view()),
    path("<int:pk>/delete/", BookDeleteApi.as_view()),
]
