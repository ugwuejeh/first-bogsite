from django.contrib import admin
from .models import Author, post, Category, Comments, ProfileModel

# Register your models here.
admin.site.register(ProfileModel)


@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
        list_display = ('name', 'slug',)
        
        
        
@admin.register(Author)
class Authoradmin(admin.ModelAdmin):
        list_display = ('profile', 'user', 'display_name',)

        
@admin.register(post)
class Postadmin(admin.ModelAdmin):
        list_display = ('title', 'body', 'upload_image', 'date_created', 'updated_on', 'author', 'category', 'status')
        
@admin.register(Comments)
class Authoradmin(admin.ModelAdmin):
        list_display = ('commenter_name', 'comment_body', 'date_created', 'user', 'Post', 'date_created' )