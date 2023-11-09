from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from bloghome.models import Category, post, Author, Comments
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
 

categories = Category.objects.all()


class create_post(LoginRequiredMixin, View):
    login_url = 'login'
    
    def get(self, request):
        context = {
            'category': categories
        }
        return render(request, 'crud/create_post.html', context=context)
    
    def post(self, request):
        post_title = request.POST['title']
        post_body = request.POST['body']
        postimages = request.FILES.get('upload_image')
        catee = request.POST['category']
        try:
            categories = Category.objects.get(slug=catee)
        except Category.DoesNotExist:
            return HttpResponse('category does not excist')
        
        createpoost = post.objects.create(title=post_title, body=post_body, 
                                          upload_image=postimages,
                                          category=categories, 
                                          author=request.user)
        createpoost.save()
        # return HttpResponse('Post created succesfully')
        return redirect('index')


class comment(View):
    def get(self, request, pk):
        
        users_comment = Comments.objects.filter(author=request.user)
        context = {
            'users_comment': users_comment
        }

        return render(request, 'details.html', context=context)
    
    def post(self, request, pk):
        Post = post.objects.get(pk=pk)
        author = Author.objects.get(user=request.user)
        comment = request.POST['comment']
        create_comment = Comments.objects.create(Post=Post, user=author, comment_body=comment)
        if create_comment:
            return redirect('details', pk=pk)
        
        return render(request, 'details.html')
    

# class updpost(LoginRequiredMixin, UpdateView):
#     model = post
#     template_name = 'crud/edit_post.html'
#     fields = ['title', 'body', 'category', 'upload_image']  # Fields that can be updated

#     def get_queryset(self):
#         # Ensure that the queryset only includes posts authored by the current user
#         return post.objects.filter(author=self.request.user)
    
    
    
    
    
# class postUpdate(View):
#     def get(self, request, pk):
#         return render(request, 'crud/update_post.html')
    
#     def post(self, request, pk):
#         if request.method == 'POST':
#             post.title = request.POST['title']
#             post.body = request.POST['body']
#             post.save()
            
#             return redirect('details', pk=pk)
            
#         return render(request, 'crud/update_post.html')