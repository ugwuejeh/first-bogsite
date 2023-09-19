from django.shortcuts import render
# from django.views.generic import TemplateView
from django.views.generic import View
from .models import  post, Category 
import pdb
# Create your views here.
# class index(TemplateView):
#     template_name = 'index.html'



class index(View):
    def get(self, request):
        
        Post_by_cat = post.objects.filter(category__name='features post')
      
        Post = post.objects.all()
        # pdb.set_trace()
        context = {
            
            "allpost": Post,
            'Post_by_cat': Post_by_cat
            
        }
    
        return render(request, "index.html", context=context)
   
    def Post(self, request):
        return render(request, "index.html")
   
#     post = Post.objects.all()
#    # Pdb.set_trace()
