from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Author, Post
from django.views import View
from django.urls import reverse_lazy
from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


# def check(request):
#     return HttpResponse("hello new project")

from django.views.generic import (
     UpdateView,
     CreateView,
     ListView,
     DeleteView,
)

class Blog(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
            blog=Post.objects.all()
            serializer=PostSerializer(blog,many=True)
            return Response(serializer.data)
    
    
   
    def post(self,request):

        #----bulk create----

        blogs=request.data
        bulk_create=[Post(**blog) for blog in blogs ]
        Post.objects.bulk_create(bulk_create)
        return Response(status=status.HTTP_201_CREATED)
    
     #----------create-------
             
        print("hello",request.data)
        title = request.data.get("Post_title")
        content = request.data.get("Post_content")
        Post.objects.create(Post_title=title,Post_content=content)



        #-----get_or_create-------
        title = request.data.get("Post_title")
        content = request.data.get("Post_content")

        post, created = Post.objects.get_or_create(
        Post_title=title,
        defaults={"Post_content": content}
        )

        serializer = PostSerializer(post)

        return Response(serializer.data)

       #-----serializer-------
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

       
    

    #bulk update
    def put(self,request,id):
        print("hello",request.data)

        blogs=Post.objects.all()[:2]
        for blog in blogs:
            blog.Post_content="automate"
            blog.Post_title="n88n"
        Post.objects.bulk_update(blogs,['Post_content','Post_title'])


    #-----------update or create--------

        title = request.data.get("Post_title")
        content = request.data.get("Post_content")

        post, created = Post.objects.update_or_create(
            Post_title=title,   
            defaults={"Post_content": content}  
        )

        serializer = PostSerializer(post)
        return Response(serializer.data)


        #----simple update---------.
        blog=request.data
        title = request.data.get("Post_title")
        content = request.data.get("Post_content")
        blog=Post.objects.get(pk=id)
        blog.Post_title=request.data.get("Post_title")
        blog.Post_content=request.data.get("Post_content")
        blog.save()
        return Response(status=status.HTTP_200_OK)
    




    #------delete-----------
    def delete(self,request,id):
        blog=Post.objects.get(pk=id)
        blog.delete()
        return Response("post deleted")
    



    


