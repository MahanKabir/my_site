
from django import forms
from .models import Episode

class EpisodeForm(forms.ModelForm):

    class Meta:
        model = Episode
        fields = ['title', 'name', 'time', 'body', 'video']
