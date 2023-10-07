from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/signin', views.signin, name='signin'),
    path('auth/signup', views.signup, name='signup'),
]