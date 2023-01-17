from rest_framework import serializers
from .models import Category, Blog



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["id", "name"]
        


class BlogSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Blog 
        fields = ["id", "title", "content", "category", "created_date", "is_published", "updated_date" ]

