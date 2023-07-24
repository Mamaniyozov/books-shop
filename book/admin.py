from django.contrib import admin

# Register your models here.

from .models import Book, Author, Book, Genre, Language, Publisher, BookImage

admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(BookImage)