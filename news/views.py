from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from .models import Article, Category, Author


def home_view(request):
    query = request.GET.get('q', '').strip()
    articles = Article.objects.filter(is_published=True).order_by('-published_date')
    if query:
        articles = articles.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(summary__icontains=query)
        )
    categories = Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories,
        'query': query,
    }
    return render(request, 'news/home.html', context)


def article_detail_view(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    categories = Category.objects.all()
    context = {
        'article': article,
        'categories': categories,
    }
    return render(request, 'news/article_detail.html', context)


def category_list_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category, is_published=True).order_by('-published_date')
    categories = Category.objects.all()
    context = {
        'category': category,
        'articles': articles,
        'categories': categories,
    }
    return render(request, 'news/category_list.html', context)
