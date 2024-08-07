from django.shortcuts import render, HttpResponse
from .models import Yangilik
# Create your views here.

def home(request):
    yangiliklar = Yangilik.objects.all()

    context = {
        'news': yangiliklar
    }

    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def category(request):
    return render(request, 'main/category.html')

def search(request):
    return render(request, 'main/search-resulthtml')

def singlepost(request):
    return render(request, 'main/single-post.html')
