from django.urls import path
from bloghome.views import index, Blog_Details, Category_list
from user.views import Login
from dele.views import updpost


urlpatterns = [
  path('', Login.as_view(), name='login'),
  path('home/', index.as_view(), name='index'),
  path('updpost/<int:pk>', updpost, name='updpost'),
  path('detail_blog/<int:pk>', Blog_Details.as_view(), name='details'),    
  path('category/<slug:category_slug>', Category_list.as_view(), name='cat'),
      
    ] 
