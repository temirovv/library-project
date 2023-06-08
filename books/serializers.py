from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'isbn', 'price')

    def validate(self, data, *args, **kwargs):
        title = data.get('title', None)
        isbn = data.get('isbn', None)
        price = data.get('price', None)

        if not title.isalpha():
            raise ValidationError(
                {
                    'status': 'error',
                    'message': "Kitob sarlavhasi harflardan iborat bo'lishi kerak"
                }
            )    
    
        if Book.objects.filter(isbn=isbn).exists():
            raise ValidationError(
                {
                    'status': 'error',
                    'message': 'siz kiritgan Kitob ISBN allaqachon mavjud!'
                }
            )
        
    
    
        if price < 0 and price > 9999999:
            raise ValidationError(
                {
                    'status': "error",
                    'message': "Narx noto'g'ri kiritilgan"
                }
            )

        return data