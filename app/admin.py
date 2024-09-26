from django.contrib import admin

from app.models import Post, Book
from modeltranslation.admin import TranslationAdmin


# Register your models here.

@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title', 'created_at',)
    search_fields = ('title',)


@admin.register(Book)
class BookAdmin(TranslationAdmin):
    list_display = ('book_name',)
    search_fields = ('book_name',)
