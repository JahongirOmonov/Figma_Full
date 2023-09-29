# from django.shortcuts import render, get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializer import AuthorSerializer, BookSerializer,CategorySerializer,AuthorSerializerDetail,BookSerializerDetail,AuthorSerializerCreate,BookSerializerCreate
# from .models import AuthorModel, BookModel,CategoryModel
# from django.http import JsonResponse
# from rest_framework import status
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from .permissions import AdminPermissionClass,WriterPermissionClass,OwnerPermission,AdminOrWriterPermissionClass

# # Create your views here.



#     #book
# class getallBooks(generics.ListAPIView):
#     queryset=BookModel.objects.all()
#     serializer_class=BookSerializer
#     permission_classes=(IsAuthenticated,)

# class postBook(generics.CreateAPIView):
#     queryset=BookModel.objects.all()
#     serializer_class=BookSerializerCreate
#     permission_classes=(IsAuthenticated,AdminOrWriterPermissionClass)
# class patchBook(generics.RetrieveUpdateDestroyAPIView):
#     queryset=BookModel.objects.all()
#     serializer_class=BookSerializerDetail
#     permission_classes=(IsAuthenticated,OwnerPermission)
#   #author
# class getallauthor(generics.ListAPIView):
#     queryset=AuthorModel.objects.all()
#     serializer_class=AuthorSerializer
#     permission_classes=(IsAuthenticated,)

# class postAuthor(generics.CreateAPIView):
#     queryset=AuthorModel.objects.all()
#     serializer_class=AuthorSerializerCreate
#     permission_classes=(IsAuthenticated,AdminOrWriterPermissionClass)
    
# class patchAuthor(generics.RetrieveUpdateDestroyAPIView):
#     queryset=AuthorModel.objects.all()
#     serializer_class=AuthorSerializerDetail
#     permission_classes=(IsAuthenticated,OwnerPermission)
    
# #category
# class getCategory(generics.ListAPIView):
#     queryset=CategoryModel.objects.all()
#     serializer_class=CategorySerializer
#     permission_classes=(IsAuthenticated,)

# class postCategory(generics.CreateAPIView):
#     queryset=CategoryModel.objects.all()
#     serializer_class=CategorySerializer
#     permission_classes=(IsAuthenticated,AdminPermissionClass)
    
# class patchCategory(generics.RetrieveUpdateDestroyAPIView):
#     queryset=CategoryModel.objects.all()
#     serializer_class=CategorySerializer
#     permission_classes=(IsAuthenticated,AdminPermissionClass)

# #Author bo'yicha barcha kitoblarni olish
# class getAuthorID(APIView):
#     def get(self, request, *args, **kwargs):
#         if str(request.user)!='AnonymousUser':
#             all=BookModel.objects.filter(author=kwargs['forid'])
#             serializer = BookSerializer(all, many=True)
#             return Response(serializer.data)

# #Categoriya bo'yicha barcha kitoblarni olish
# class getCategoryID(APIView):
#     def get(self, request, *args, **kwargs):
#         if str(request.user)!='AnonymousUser':
#             all=BookModel.objects.filter(category=kwargs['forid'])
#             serializer = BookSerializer(all, many=True)
#             return Response(serializer.data)

# #Categoriya bo'yicha barcha shoirlarni olish
# class getCategoryIDAuthor(APIView):
#     def get(self, request, *args, **kwargs):
#         if str(request.user)!='AnonymousUser':
#             all=AuthorModel.objects.filter(category=kwargs['forid'])
#             serializer = AuthorSerializer(all, many=True)
#             return Response(serializer.data)


# >>>>

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import AuthorSerializer, BookSerializer,CategorySerializer,AuthorSerializerDetail,BookSerializerDetail,AuthorSerializerCreate,BookSerializerCreate
from .models import AuthorModel, BookModel,CategoryModel
from django.http import JsonResponse
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import AdminPermissionClass,WriterPermissionClass,OwnerPermission,AdminOrWriterPermissionClass

# Create your views here.



    #book
class getallbooks(generics.ListAPIView):
    queryset=BookModel.objects.all()
    serializer_class=BookSerializer
    permission_classes=(IsAuthenticated,)

class postBook(generics.CreateAPIView):
    queryset=BookModel.objects.all()
    serializer_class=BookSerializerCreate
    permission_classes=(IsAuthenticated,AdminOrWriterPermissionClass)
class patchBook(generics.RetrieveUpdateDestroyAPIView):
    queryset=BookModel.objects.all()
    serializer_class=BookSerializerDetail
    permission_classes=(IsAuthenticated,OwnerPermission)
  #author
class getallauthor(generics.ListAPIView):
    queryset=AuthorModel.objects.all()
    serializer_class=AuthorSerializer
    permission_classes=(IsAuthenticated,)

class postAuthor(generics.CreateAPIView):
    queryset=AuthorModel.objects.all()
    serializer_class=AuthorSerializerCreate
    permission_classes=(IsAuthenticated,AdminOrWriterPermissionClass)
    
class patchAuthor(generics.RetrieveUpdateDestroyAPIView):
    queryset=AuthorModel.objects.all()
    serializer_class=AuthorSerializerDetail
    permission_classes=(IsAuthenticated,OwnerPermission)
    
#category
class getCategory(generics.ListAPIView):
    queryset=CategoryModel.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(IsAuthenticated,)

class postCategory(generics.CreateAPIView):
    queryset=CategoryModel.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(IsAuthenticated,AdminPermissionClass)
    
class patchCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset=CategoryModel.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(IsAuthenticated,AdminPermissionClass)

#Author bo'yicha barcha kitoblarni olish
class getAuthorID(APIView):
    def get(self, request, *args, **kwargs):
        if str(request.user)!='AnonymousUser':
            all=BookModel.objects.filter(author=kwargs['forid'])
            serializer = BookSerializer(all, many=True)
            return Response(serializer.data)

#Categoriya bo'yicha barcha kitoblarni olish
class getCategoryID(APIView):
    def get(self, request, *args, **kwargs):
        if str(request.user)!='AnonymousUser':
            all=BookModel.objects.filter(category=kwargs['forid'])
            serializer = BookSerializer(all, many=True)
            return Response(serializer.data)

#Categoriya bo'yicha barcha shoirlarni olish
class getCategoryIDAuthor(APIView):
    def get(self, request, *args, **kwargs):
        if str(request.user)!='AnonymousUser':
            all=AuthorModel.objects.filter(category=kwargs['forid'])
            serializer = AuthorSerializer(all, many=True)
            return Response(serializer.data)