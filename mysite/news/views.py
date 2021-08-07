from django.shortcuts import render
from django.http import HttpResponse

from news.models import News


def index(request):
    news = News.objects.order_by('-created_at')
    # res = '<h1>Список новостей</h1>'
    # for item in news:
    #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n<hr>\n'
    # return HttpResponse(res)
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template_name='news/index.html', context=context)
