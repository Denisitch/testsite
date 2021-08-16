from django.views.generic import ListView, DetailView, CreateView
from news.models import News, Category
from news.forms import NewsForm
from news.utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(MyMixin, ListView):
    model = Category
    template_name = 'news/index.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsByCategory, self).get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(LoginRequiredMixin, DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'item_news'
    login_url = '/admin/'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
