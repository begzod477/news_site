from django.shortcuts import render, get_object_or_404
from .models import Category, News

# Create your views here.
def home(request):
    categories = Category.objects.all()
    news = News.objects.all()
    return render(request, 'news/home.html', {'categories': categories, 'news': news})

def category_detail(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    news = News.objects.filter(category=category)
    return render(request, 'news/home.html', {'categories': categories, 'news': news})

def news_detail(request, news_id):
    categories = Category.objects.all()
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'news/news_detail.html', {'categories': categories, 'news': news_item})
