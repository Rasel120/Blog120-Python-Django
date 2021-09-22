from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    path('postcom', views.postcomment, name='postcom'), 

    path('', views.bloghome, name='bloghome'),
    path('<str:slug>/', views.blogpost, name='blog'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'), #Here search/ is just a name

]