from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'), #yangilik.uz/about
    path('contact', contact, name='contact'),
    path('category', category, name='category'),
    path('search-result', search, name='search'),
    path('single-post', singlepost, name='single')
]