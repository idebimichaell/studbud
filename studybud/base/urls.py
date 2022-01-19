from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name="index"),
    path('logout/', views.logoutUser, name="logout"),
    path('addcourse/', views.addcourse, name="addcourse"),
    path('editcourse/<str:pk>/', views.updatecourse, name="editcourse"),
    path('deletecourse/<str:pk>/', views.deletecourse, name="deletecourse"),
    path('outline/<str:pk>/', views.outline, name="outline"),
    path('updatetopic/<str:pk>/', views.updatetopic, name="updatetopic"),
    path('deletetopic/<str:pk>/', views.deletetopic, name="deletetopic"),
    path('chat/<str:pk>/', views.chat, name="chat"),
    #path('getpdf/<str:pk>/', views.getpdf, name="getpdf"),
    path('profile/', views.profile, name="profile"),
    path('signup/', views.signup, name="signup"),

]

urlpatterns += staticfiles_urlpatterns()