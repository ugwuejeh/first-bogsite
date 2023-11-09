from django.urls import path
from user.views import Signup, Logout
from user.views import delete_post, profile

urlpatterns = [
  path('', Signup.as_view(), name='signup'),
  path('profile/', profile, name='user_profile'),
  path('logout/', Logout, name='logout'),
  path('delete_update/<int:pk>', delete_post, name='delete_update'),

      
    ] 
