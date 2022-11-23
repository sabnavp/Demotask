from .import views
from django.urls import path

urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about'),
    path('new',views.new,name='new'),
    path('sub',views.sub,name='sub'),
    path('index', views.index, name='index'),
    ]