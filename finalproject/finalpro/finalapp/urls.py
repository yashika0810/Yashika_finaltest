from django.urls import path
from finalapp import views

urlpatterns = [
    path('', views.userpro, name='index'),
    path('int:id>', views.userprofile),
    path('edit/', views.create, name='edit'),
    path('api/', views.view_data.as_view()),
   
  

    ]