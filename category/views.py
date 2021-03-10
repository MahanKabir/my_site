from django.shortcuts import render, redirect
from .forms import CategoryForm

# Create your views here.

def create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user_id = request.user.id
            f.save()
            # return redirect()

    return render(request, 'category/create.html')

def read(request):
    pass

def update(request, category_id):
    pass

def delete(request, category_id):
    pass