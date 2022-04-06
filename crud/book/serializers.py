from rest_framework import serializers
from .models import Books
from django.contrib.auth.models import User



class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
