from django.contrib import admin
from .models import *

# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'publisher', 'language')
    list_display_links = ('book_title', 'language')
    search_fields = ('book_title', 'language')

class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'country')
    list_display_links = ('full_name', 'country')
    search_fields = ('full_name', 'country')

class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'date_created', 'reviewer', 'content')

admin.site.register(Books, BooksAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)

