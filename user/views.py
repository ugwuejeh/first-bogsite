from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from bloghome.models import post
from bloghome.forms import postupdateForm


class Signup(View):
    def get(self, request):
        return render(request, 'registration/signup.html')
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        confirm_password = request.POST['password2']

        if password != confirm_password:
            return HttpResponse('Password not the same')
        
        if len(username) < 5:
            return HttpResponse('Username must be more than 5 character')
        
        if User.objects.filter(username=username).exists():
            return HttpResponse('username already taken')
        
        user = User.objects.create_user(username=username, email=email,
                                        first_name=firstname,
                                        last_name=lastname)
        user.set_password(password)
        user.save()
        user = authenticate(request, username=username, password=password)
        login(request, user)
        # return HttpResponse('account created successfully')
        return redirect('login')


class Login(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        if not User.objects.filter(username=username).exists():
            return HttpResponse('Username not found. Please try again with a correct user. If you have not signed up yet, please sign up to log in')
     
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
            return redirect('index')
        
        if not User.objects.filter(password=password).exists():
            return HttpResponse('incorrect password try again')
        

def Logout(request):
    logout(request)
    return redirect('login')


# def post_update(request, pk):        
#     post_instance = post.objects.get(pk=pk)
#     if request.method == "POST":
#         form = postupdateForm(request.POST, instance=post_instance)
#         if form.is_valid():
#             form.save()
#             return redirect('details', pk=pk) 
#     else:
#         form = postupdateForm(instance=post_instance)
#     context = {
#         'post_instance': post_instance,
#         'form': form,
#     }
#     return render(request, 'crud/update_post.html', context)

# Fuction to delete post on line 84 of user app


def delete_post(request, pk):
    pst =post.objects.get(pk=pk)
    if request.method == 'POST':
        pst.delete()
        return redirect('index')
    
    context = {
        'post': pst
    }
    return render(request, 'crud/delete_post.html', context)

# Fuction to create profile on line 98 of user app


def profile(request):
    return render(request, 'registration/profile.html')

