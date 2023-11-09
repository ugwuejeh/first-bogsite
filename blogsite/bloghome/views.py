# from typing import Any
# from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.views.generic import View, ListView, DetailView
# from .forms import PostForm
from .models import post, Category, Author, Comments


class index(View):
    def get(self, request):
        # try:
        #     Author.objects.get(user=request.user)
        # except Author.DoesNotExist:
        #     return redirect('')
        
        try:
            Post_by_cat = post.objects.filter(category__name='Politics',
                                              status='approved').latest('date_created')
        except: Post_by_cat =None
        
        approved_post = post.objects.filter(status='approved')
        pending_post = post.objects.filter(status='pending')
        user_pendingpost = post.objects.filter(author=request.user, status='pending')
        Post_by_users = post.objects.filter(author=request.user)
        # users_comment = Comments.objects.filter(user=request.user)

        context = {
            
            "allpost": approved_post,
            'Post_by_cat': Post_by_cat,
            'pending_post': pending_post,
            'user_pendingpost': user_pendingpost,
            'Post_by_users': Post_by_users,
            # 'users_comment': users_comment
        }
    
        return render(request, "index.html", context=context)
   
    def Post(self, request):
        return render(request, "index.html")
   
#     post = Post.objects.all()
#    # Pdb.set_trace()


class Blog_Details(ListView):
    def get(self, request, pk):
        post_details = get_object_or_404(post, pk=pk)
        context = {
            'post_details': post_details
        }
        return render(request, "details.html", context=context)
     
    def Post(self, request, pk):
        post_details = get_object_or_404(post, pk=pk)
        context = {
            'post_details': post_details
        }
    
        return render(request, "details.html", context=context)
    
    
class Category_list(DetailView):
    def get(self, request, category_slug):
        cate_list = Category.objects.get( slug=category_slug)
        cattegory_by_post = post.objects.filter(category=cate_list)
        contexta = {
                'cattegory_by_post': cattegory_by_post,
                'cat_list': cate_list
            }
        return render(request, "category/cat_list.html", context=contexta)
    
    def Post(self, request):
        return render(request, "categorycat_list.html")