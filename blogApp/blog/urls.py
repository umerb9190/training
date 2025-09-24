from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .views import(
    # # create_blog,
    # show_all,
    # update_blog,
    # delete_blog,
    Blog
    
)  


urlpatterns = [
    
    # path('', views.check, name='check'),
    path('blog/',Blog.as_view(),name='blog'),
    # path('show',show_all.as_view(),name='show'),
    # path('update/<int:pk>',update_blog.as_view(),name='update_blog'),
    # path('delete/<int:pk>',delete_blog.as_view(),name='delete_blog'),
    path('blog/<int:id>/',Blog.as_view(),name='update_blog'),
    path('login/',TokenObtainPairView.as_view(), name="token_obtain_pair")
    # path('blog/<int:id>/',Blog.as_view(),name='delete_blog')
    # path('show',views.show_all,name='show_all'),
    # path('update/<int:dubai>',views.update_blog,name='update_blog'),
    #  path('delete/<int:id>',views.delete_blog,name='delete_blog')
]