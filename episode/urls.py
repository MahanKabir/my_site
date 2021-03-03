from django.urls import path
from . import views




urlpatterns = [
    path('create', views.create, name="create.episode"),#localhost:8000/episode/create
    path('read', views.read, name="read.episode"),#localhost:8000/episode/read
    path('update/<int:episode_id>', views.update, name="update.episode"),#localhost:8000/episode/update
    path('delete/<int:episode_id>', views.delete, name="delete.episode"),#localhost:8000/episode/delete
]