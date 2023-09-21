from django.urls import path
from bloghome.views import index, Blog_Details


urlpatterns = [
    
      path('', index.as_view(), name='index'),
      
      path('detail_blog/<int:pk>', Blog_Details.as_view(), name='details')
    ] 
