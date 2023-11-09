from django.shortcuts import get_object_or_404, render, redirect
from bloghome.models import post

# Fuction to  update post on line 5 of dele app


def updpost(request, pk):
    Post = get_object_or_404(post, pk=pk)
    
    if request.method == 'POST':
        Post.title = request.POST.get('title')
        Post.body = request.POST.get('body')
        uploaded_image = request.FILES.get('upload_image')
        if uploaded_image:
            Post.upload_image = uploaded_image
        Post.save()
        return redirect('details', pk=pk)  # Redirect to the post detail page after update
        
    return render(request, 'crud/edit_post.html', {'Post': Post})
