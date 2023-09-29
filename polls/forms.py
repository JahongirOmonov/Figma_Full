from django import forms
from .models import BookModel, AuthorModel, CategoryModel


class BookForm(forms.ModelForm):
    name_uz=forms.CharField()
    name_en=forms.CharField()
    name_ru=forms.CharField()

    
    description_uz=forms.CharField()
    description_en=forms.CharField()
    description_ru=forms.CharField()

    class Meta:
        model=BookModel
        exclude=('name', 'description')

class CategoryForm(forms.ModelForm):
    name_uz=forms.CharField()
    name_en=forms.CharField()
    name_ru=forms.CharField()

    

    class Meta:
        model=CategoryModel
        exclude=('name',)


class AuthorForm(forms.ModelForm):
    name_uz=forms.CharField()
    name_en=forms.CharField()
    name_ru=forms.CharField()

    surname_uz=forms.CharField()
    surname_en=forms.CharField()
    surname_ru=forms.CharField()

    
    description_uz=forms.CharField()
    description_en=forms.CharField()
    description_ru=forms.CharField()

    class Meta:
        model=AuthorModel
        exclude=('name', 'surname', 'description')