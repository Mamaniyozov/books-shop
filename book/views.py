from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from book.models import Genre, Book, BookImage, Publisher, Author, Language
from .serializers import PostSerializer

class UserView(APIView):
    def get(self,request,id:int):
        try:
            user=User.objects.get(id=id)
            return Response({ "username": user.username, "first_name": user.first_name, "last_name": user.first_name})
        except:
            return Response({'result':'User not found'})
        

class Users(APIView):
    def get(self,request):
        try:
            data=[]
            users=User.objects.all()
            for user in users:
                data.append({ "username": user.username, "first_name": user.first_name, "last_name": user.first_name})
            return Response(data)
        except:
            return Response({'result':'Users not found'})
        

class PostsView(APIView):
    def get(self, request: Request) -> Response:
        posts = Book.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response({"posts": serializer.data})
    

class PostView(APIView):
    def get(self, request: Request, id: int) -> Response:
        try:
            post = Book.objects.get(id=id)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Status": "This post doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
        

class Createbook(APIView):
    def post(self,request):
        data=request.data
        username=data.get('username', None)
        password=data.get('password', None)
        if username==None or password==None:
            return Response({'result':'didn\'t input required data'})
        try:
            user=User.objects.get(username=username)
            return Response({'result':'Invalid username'})
        except:
            user=Book.objects.create(
                title = data.get('title'),
                authors = data.get('authors'),
                publisher = data.get('publisher'),
                publication_date = data.get('publication_date'),
                genres = data.get('genres'),
                description = data.get('description'),
                cover = data.get('cover'),
                price = data.get('price')
            )
            user.save()
            return Response({ "message": "User created successfully." },status=status.HTTP_201_CREATED)
        

class Updatebook(APIView):
    def put(self,request,id:int):
        data=request.data
        try:
            user=Book.objects.get(id=id)
            user.title = data.get('title')
            user.authors = data.get('authors')
            user.publisher = data.get('publisher')
            user.publication_date = data.get('publication_date')
            user.genres = data.get('genres')
            user.description = data.get('description')
            user.cover = data.get('cover')
            user.price = data.get('price')
            user.save()
            return Response({ "message": "User updated successfully." },status=status.HTTP_200_OK)
        except:
            return Response({'result':'User not found'})
        

class Deletebook(APIView):
    def delete(self,request,id:int):
        try:
            user=Book.objects.get(id=id)
            user.delete()
            return Response({ "message": "User deleted successfully." },status=status.HTTP_200_OK)
        except:
            return Response({'result':'User not found'})
        
