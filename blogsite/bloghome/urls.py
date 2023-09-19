from django.urls import path
from bloghome.views import index


urlpatterns = [
    
      path('', index.as_view(), name='index'),
    ] 
