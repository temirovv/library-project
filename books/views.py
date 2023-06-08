from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError


# class BookDetailApi(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDetailApi(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            book = Book.objects.get(id=pk)
            serializer = BookSerializer(book).data
            data = {
                'status': True,
                'book': serializer
            }
            return Response(data, status=status.HTTP_200_OK)
        
        except Exception:
            data = {
                'status': False,
                'book': "Not Found :("
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)


# class BookUpdateApi(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookUpdateApi(APIView):

    def put(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(isinstance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
                "status": True,
                "message": f"Book {book_saved} updated succesfully"
            }
        )


# class BookDeleteApi(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDeleteApi(APIView):
    def delete(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book.objects.all(), id=pk)
        book.delete()
        return Response(
            {
                "status": True,
                "message": "Book succesfully deleted!"
            }
        )


# class BookCreateApi(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookCreateApi(generics.CreateAPIView):

    def get_serializer_class(self):
        return BookSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            context_data = {
                'status': "Books have been successfully saved",
                'books': data
            }
            return Response(context_data)


class BookListApi(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f"Returned {len(books)} books",
            "books": serializer_data
        }
        return Response(data)
    

class BookListCreateApi(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer