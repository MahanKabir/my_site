from django.urls import path

from . import views

urlpatterns = [
    path('create', views.create, name="create.category"), #localhost:8000/category/create
    path('read', views.read, name="read.category"), #localhost:8000/category/read
    path('update/<int:category_id>', views.update, name="update.category"), #localhost:8000/category/update/id
    path('delete/<int:category_id>', views.delete, name="delete.category"), #localhost:8000/category/delete/id
]