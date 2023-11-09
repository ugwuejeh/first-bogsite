from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
# Create your models here.

 
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, max_length=300,)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
         
    def __str__(self):
        return self.name
    
    
class Author(models.Model):
    profile = models.ImageField(upload_to='image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.display_name
    
    
post_status = (
        ('pending', 'pending'),
        ('delete', 'delete'),
        ('approved', 'approved')
    )


class post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(max_length=1000)
    upload_image = models.ImageField(upload_to='post')
    date_created = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    status = models.CharField(choices=post_status,default='pending',max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Mata:
        ordering = ['-date_created']
        
    
class Comments(models.Model):
    Post = models.ForeignKey(post, related_name='comments', on_delete=models.CASCADE)
    comment_body = models.TextField(max_length=400)
    commenter_name = models.TextField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
   
    
    
    def __str__(self):
        return self.comment_body
    
    
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    upload_image = models.ImageField(default='default.png', upload_to='post', 
                                     validators=[FileExtensionValidator(['png', 'jpg'])])
    
    
    
    def __str__(self):
        return self.user.username