from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogIndex, name='blog'),
    path('blogDetails/', views.blogDetails, name='blogDetails'),
    path('blogSearch/', views.blogSearch, name='blogSearch'),
    path('popularTag/', views.popularTag, name='popularTag'),
    path('toBlogCreation/', views.toBlogCreation, name='toBlogCreation'),
    path('blogCreation/', views.blogCreation, name='blogCreation'),
    path('addComment/', views.addComment, name='addComment'),
    path('toLogin/', views.toLogin, name='toLogin'),
    path('login/', views.login, name='login'),
    path('toLogout/', views.toLogout, name='toLogout'),
    path('toRegister/', views.toRegister, name='toRegister'),
    path('register/', views.register, name='register'),
    path('toPersonal/', views.toPersonal, name='toPersonal'),
    path('toForgetPassword/', views.toForgetPassword, name='toForgetPassword'),
    path('forgetPassword/', views.forgetPassword, name='forgetPassword'),
    path('updateBlogUser/', views.updateBlogUser, name='updateBlogUser'),
    path('updateHeader/', views.updateHeader, name='updateHeader'),
    path('toNavigation/', views.toNavigation, name='toNavigation'),
    path('uploadFile/', views.uploadFile, name='uploadFile'),
]