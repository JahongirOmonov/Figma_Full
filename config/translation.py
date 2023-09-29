from modeltranslation.translator import translator, TranslationOptions
from polls.models import BookModel, AuthorModel, CategoryModel

class BookTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
    required_languages = ('uz',)


translator.register(BookModel, BookTranslationOptions)

class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'description')
    required_languages = ('uz',)


translator.register(AuthorModel, AuthorTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = ('uz',)


translator.register(CategoryModel, CategoryTranslationOptions)