from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from user  import views
from rest_framework.authtoken.views import obtain_auth_token # token-auth

# from account import views
router =routers.DefaultRouter()
router.register('adminaccount',views.AccountAPI ,basename='adminaccount')


urlpatterns = [
    path('',include(router.urls)),
    path('token-auth/', obtain_auth_token, name='api_token_auth'), # token-auth
    path('login/',views.UserAuthAPI.as_view()),
]