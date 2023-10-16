from django.contrib import admin
from .models import Publisher,Author,Book ,BookImage,Genre,Language
admin.site.register([
    Publisher,
    Author,
    Book,
    BookImage,
    Genre,
    Language
])
# Register your models here.

from .models import Book, Author, Book, Genre, Language, Publisher, BookImage

admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(BookImage)