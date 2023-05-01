from django.shortcuts import render

from . models import Category

# Create your views here.

def store(request):
    pass
    return render(request, 'store/store.html')
    #return render(request, 'store.html')
    
    
def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}    
