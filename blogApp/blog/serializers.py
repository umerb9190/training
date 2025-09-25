from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_Post_title(self,data):
       if "@" in data:
        raise serializers.ValidationError("Title cannot contain @ symbol")
         
       return data