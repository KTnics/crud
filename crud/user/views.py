from rest_framework import response,viewsets
from django.contrib.auth.models import User
from . import serializers as UserModelSerializer
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import authentication, permissions

class AccountAPI(viewsets.ViewSet):
    serializer_class=UserModelSerializer.ProfileSerializer
    queryset=User.objects.all()

    def list(self,request):
        serializer=self.serializer_class(self.queryset,many=True)
        return response.Response(serializer.data)

    def create(self,request):
        username = request.data['username']
        first_name =request.data['first_name']
        last_name =request.data['last_name']
        email = request.data['email']
        password = request.data['password']
        user= User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )
        user.set_password(password)
        user.save()
        return response.Response(status=200)


# ---
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class UserAuthAPI(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES