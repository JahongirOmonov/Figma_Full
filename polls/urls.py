# from django.urls import path
# from .views import getallauthor, getallBooks, getAuthorID, postAuthor, postBook, patchAuthor, patchBook,getCategory,postCategory,patchCategory,getCategoryID,getCategoryIDAuthor

# urlpatterns=[
#     path('getcategoryID/<int:forid>', getCategoryID.as_view()),
#     path('getcategoryIDauthor/<int:forid>', getCategoryIDAuthor.as_view()),
#     path('getAuthorID/<int:forid>', getAuthorID.as_view()), #Author ID sini kiritsa kitoblarini chiqarib beradi
#     #pasdagi qismlar CRUD >>>
#     path('postauthor/', postAuthor.as_view()),
#     path('postbook/', postBook.as_view()),
#     path('patchauthor/<int:pk>', patchAuthor.as_view()),
#     path('patchbook/<int:pk>', patchBook.as_view()),
#     path('getallauthors/', getallauthor.as_view()), #hamma authorlar ro'yhati
#     path('getallBooks/', getallBooks.as_view()), #hamma kitoblar ro'yhati
#     path('getallcategory/', getCategory.as_view()),
#     path('postcategory/', postCategory.as_view()),
#     path('patchcategory/<int:pk>', patchCategory.as_view())
# ]

# #yozuvchi Jahongir77
# #fonarik  Jahongir47


from django.urls import path
from .views import getallauthor, getallbooks, getAuthorID, postAuthor, postBook, patchAuthor, patchBook,getCategory,postCategory,patchCategory,getCategoryID,getCategoryIDAuthor

urlpatterns=[
    path('getcategoryID/<int:forid>', getCategoryID.as_view()),
    path('getcategoryIDauthor/<int:forid>', getCategoryIDAuthor.as_view()),
    path('getAuthorID/<int:forid>', getAuthorID.as_view()), #Author ID sini kiritsa kitoblarini chiqarib beradi
    #pasdagi qismlar CRUD >>>
    path('postauthor/', postAuthor.as_view()),
    path('postbook/', postBook.as_view()),
    path('patchauthor/<int:pk>', patchAuthor.as_view()),
    path('patchbook/<int:pk>', patchBook.as_view()),
    path('getallauthors/', getallauthor.as_view()), #hamma authorlar ro'yhati
    path('getallbooks/', getallbooks.as_view()), #hamma kitoblar ro'yhati
    path('getallcategory/', getCategory.as_view()),
    path('postcategory/', postCategory.as_view()),
    path('patchcategory/<int:pk>', patchCategory.as_view())
]