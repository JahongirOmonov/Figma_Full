from django.contrib import admin
from .models import BookModel
from .models import AuthorModel,CategoryModel
from .forms import BookForm, AuthorForm, CategoryForm

class CategoryAdmin(admin.ModelAdmin):
    form=BookForm
    list_display=('name',)
    search_fields=('name',)
    prepopulated_fields={"slug":("name")}

class AuthorAdmin(admin.ModelAdmin):
    form=AuthorForm
    list_display=('name',)
    search_fields=('name',)
    prepopulated_fields={"slug":("name")}


class CategoryAdmin(admin.ModelAdmin):
    form=CategoryForm
    list_display=('name',)
    search_fields=('name',)
    prepopulated_fields={"slug":("name")}



# Register your models here.

admin.site.register(BookModel, CategoryAdmin)
admin.site.register(AuthorModel, AuthorAdmin)
admin.site.register(CategoryModel, CategoryAdmin)

