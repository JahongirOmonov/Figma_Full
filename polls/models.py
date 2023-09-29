from django.db import models
from datetime import datetime
from account.models import CustomUser


# Create your models here.

class CategoryModel(models.Model):
    name=models.CharField(max_length=100,default='')
    class Meta:
        db_table='category'

    def __str__(self) -> str:
        return self.name


class AuthorModel(models.Model):
    name=models.CharField(max_length=100, default='')
    surname=models.CharField(max_length=100, default='')
    date_of_birth=models.DateTimeField(default=datetime.now)
    date_of_death=models.DateTimeField(default=datetime.now)
    alive=models.BooleanField(default=True)
    description=models.TextField()
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    class Meta:
        db_table='author'

    def __str__(self) -> str:
        return self.name
    

class BookModel(models.Model):
    name=models.CharField(max_length=100, default='')
    page=models.PositiveIntegerField(default=3)
    year_of_invented=models.DateTimeField(default=datetime.now)
    price=models.PositiveIntegerField(default=500)
    description=models.TextField()
    author=models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table='book'

    def __str__(self) -> str:
        return self.name
    
    #Jahongir a9f79Q6WY6YyAjS
    #akmal fEJ5KgNXcT5nP8v