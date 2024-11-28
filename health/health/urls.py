
from django.urls import path, include  
from django.contrib import admin

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('app.urls')), 
    path('admin/', admin.site.urls),


]

