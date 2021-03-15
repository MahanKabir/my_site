from django.urls import path

from . import views

urlpatterns = [
    path('create/<int:category_id>', views.create, name="create.article"), #localhost:8000/article/create
    path('read/<int:category_id>', views.read, name="read.article"), #localhost:8000/article/read
    path('update/<int:article_id>', views.update, name="update.article"), #localhost:8000/article/update/id
    path('delete/<int:article_id>', views.delete, name="delete.article"), #localhost:8000/article/delete/id
]