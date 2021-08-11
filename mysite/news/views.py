from django.shortcuts import render, get_object_or_404
from news.models import News, Category


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})


def view_news(request, news_id):
    # item_news = News.objects.get(pk=news_id)
    item_news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'item_news': item_news})
