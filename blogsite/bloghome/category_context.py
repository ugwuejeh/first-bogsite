from .models import Category


def category_list(request):
    global_list = Category.objects.all()
    return {
        'global_list': global_list
        
    }