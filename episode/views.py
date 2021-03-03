from django.shortcuts import render, redirect

# Create your views here.
from episode.forms import EpisodeForm


def create(request):
    if request.method == "POST":
        form = EpisodeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('read.episode')

    return render(request, 'episode/create.html')

def read(request):
    pass

def update(request, episode_id):
    pass

def delete(request, episode_id):
    pass