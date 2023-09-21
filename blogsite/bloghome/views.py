from django.shortcuts import render, get_object_or_404
# from django.views.generic import TemplateView
from django.views.generic import View, ListView
from .models import  post, Category 
import pdb
# Create your views here.
# class index(TemplateView):
#     template_name = 'index.html'



class index(View):
    def get(self, request):
        
        Post_by_cat = post.objects.filter(category__name='features post', status='approved').latest('date_created')
        
        approved_post = post.objects.filter(status='approved')
        pending_post = post.objects.filter(status='pending')
      
        # Post = post.objects.all()
        # pdb.set_trace()
        context = {
            
            "allpost": approved_post,
            'Post_by_cat': Post_by_cat,
            'pending_post': pending_post
            
        }
    
        return render(request, "indexx.html", context=context)
   
    def Post(self, request):
        return render(request, "indexx.html")
   
#     post = Post.objects.all()
#    # Pdb.set_trace()

class Blog_Details(ListView):
    def get(self, request, pk):
        # post_details = post.objects.get(pk=pk)
        post_details =get_object_or_404(post,pk=pk)
        context = {
            'post_details': post_details
        }
        return render(request, "details.html", context=context)
    
    
    def Post(self, request, pk):
        # post_details = post.objects.get(pk=pk)
        post_details =get_object_or_404(post,pk=pk)
        context = {
            'post_details': post_details
        }
        return render(request, "details.html", context=context)