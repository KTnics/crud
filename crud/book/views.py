from rest_framework import  response,viewsets
from . import models as BooksModel
from . import serializers as BookSearializer
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from rest_framework import authentication, permissions


class BooksList(viewsets.ModelViewSet):
    authentication_classes=(authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class=BookSearializer.BooksSerializer
    queryset=BooksModel.Books.objects.all()
