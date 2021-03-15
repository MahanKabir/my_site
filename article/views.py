from django.shortcuts import render, redirect
from category.models import Category
from .models import Article
from .forms import ArticleForm

# Create your views here.


def create(request, category_id):

    category = Category.objects.get(id=category_id)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.category_id = category.id
            f.user_id = request.user.id
            f.save()
            return redirect("read.article", category.id)
    return render(request, 'article/create.html', {'category': category})

def read(request, category_id):
    category = Category.objects.get(id=category_id)
    articles = Article.objects.filter(category_id=category)
    return render(request, 'article/read.html', {'category': category, 'articles': articles})

def update(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()

    return render(request, 'article/update.html', {'article': article})

def delete(request, article_id):
    pass

