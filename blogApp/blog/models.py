from django.db import models

# Create your models here.
class Author(models.Model):
    Author_name=models.CharField(max_length=20)

    def __str__(self):
        return self.Author_name


class Post(models.Model):
    Post_title=models.CharField(max_length=30)
    Post_content=models.TextField()
    
   
    
    


