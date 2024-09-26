from modeltranslation.translator import  translator, TranslationOptions
from .models import Post, Book


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'description')  # Fields to translate


translator.register(Post, PostTranslationOptions)


class BookTranslationOptions(TranslationOptions):
    fields = ('book_name', 'description')


translator.register(Book, BookTranslationOptions)
