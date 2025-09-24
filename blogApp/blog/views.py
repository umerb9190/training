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
        # user=request.user
        # print("user " ,user)
        # print("rrrr ",serializer)
        return Response(serializer.data)
    
    def post(self,request):
        # print("hello",request.data)
        title = request.data.get("Post_title")
        content = request.data.get("Post_content")
        Post.objects.create(Post_title=title,Post_content=content)
        return Response(status=status.HTTP_201_CREATED)
        # serializer = PostSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors)
    
    def put(self,request,id):
        print("hello",request.data)
        title = request.data.get("Post_title")
        content = request.data.get("Post_content")
        blog=Post.objects.get(pk=id)
        blog.Post_title=request.data.get("Post_title")
        blog.Post_content=request.data.get("Post_content")
        blog.save()
        return Response(status=status.HTTP_200_OK)

    
    def delete(self,request,id):
        blog=Post.objects.get(pk=id)
        blog.delete()
        return Response("post deleted")
    



    


#     model=Post
#     fields=['Post_title', 'Post_content']
#     template_name='blog/create_post.html'
#     success_url = reverse_lazy('show') 


# class show_all(ListView):
#     model=Post
#     template_name='blog/showall.html'


# class update_blog(UpdateView):
#     model=Post
#     fields=['Post_title', 'Post_content']   
#     template_name = 'blog/update.html'
#     success_url = reverse_lazy('show')

# class delete_blog(DeleteView):
#     model=Post
#     success_url=reverse_lazy('show')
#     template_name = "blog/confirm_delete.html"

#     # if request.method=='POST':
    #     title=request.POST.get("title")
    #     # print("umerrr",title)
    #     content=request.POST.get("Content")
    #     author_name=request.POST.get("Author")
    #     author=Author.objects.get(Author_name=author_name)
    #     print("testing ",title)
    #     post=Post(Post_title=title,
    #               Post_content=content,
    #               A_name=author)
    #     post.save()
    #     print("post created",post)
    # return render(request,"blog/create_post.html")


# def show_all(request):
#     all_posts=Post.objects.all()
#     print("umerrr",all_posts)
#     return render(request,"blog/showall.html",{"all_posts":all_posts})

# def update_blog(request,dubai):
#     print("id",dubai)
#     blog_by_id=Post.objects.get(id=dubai)
#     # print(blog_by_id)
#     if request.method=='POST':
#         title=request.POST.get("title")
#         print("new_title",title)
#         content=request.POST.get("Content")
        
#         blog_by_id.Post_title=title
#         blog_by_id.Post_content=content
#         blog_by_id.save()
       

#         print( blog_by_id.Post_title,"after updating")
#         return redirect("show_all")
        


#     return render(request,"blog/update.html",{"blog_by_id":blog_by_id})


# def delete_blog(request,id):
#     blog=Post.objects.get(id=id)
#     print("deleting blog ",blog.Post_title)
#     blog.delete()
#     return redirect("show_all")
    
