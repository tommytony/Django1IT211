


from django.contrib import admin
from django.urls import path
from module_image import views


urlpatterns = [
    # int : nombre
    # str : caractère
    path('',views.home , name='home'), 
    path('<int:year>/<str:month>/',views.home , name='home'), 
    path('add_post', views.add_post , name='add_post'),
]
