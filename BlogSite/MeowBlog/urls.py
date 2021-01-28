from django.urls import path
from . import views
app_name = 'MeowBlog'

urlpatterns = [
    path('', views.index, name='index'),
   path('user/signup', views.createUser, name='createUser'),
   path('user/deleteaccount', views.deleteUser, name='deleteUser'),
   path('user/updateuserprofile', views.updateUser, name='updateUser'),
   path('user/userprofile', views.updateUser, name='readUser'),
   path('sentense/generatecontent', views.generateContent, name='generateContent'),
   path('sentense/viewcontent/<int:page>', views.viewContent, name='viewContent')
]