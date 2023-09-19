from django.contrib import admin
from .models import Author, post, Category

# Register your models here.
@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
        list_display = ('name',)
        
        
        
@admin.register(Author)
class Authoradmin(admin.ModelAdmin):
        list_display = ('profile', 'user', 'display_name',)

        
@admin.register(post)
class Postadmin(admin.ModelAdmin):
        list_display = ('title', 'body', 'upload_image', 'date_created', 'updated_on', 'author', 'category')
        
