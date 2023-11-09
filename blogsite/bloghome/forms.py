from django import forms
from django.forms import ModelForm
from .models import post


class PostForm(ModelForm):
    class Meta:
        model = post
        fields = '__all__'
        
        
class postupdateForm(forms.ModelForm):
    
    class Meta:
        model = post
        fields = ('title', 'body', 'category')