from django.urls import path
from usere.views import create_post, comment

urlpatterns = [
  path('', create_post.as_view(), name='createpost'),
  path('comment/<int:pk>', comment.as_view(), name='comment'),
  # path('updpost/<int:pk>/', updpost.as_view(), name='updpost'),
  
    ] 