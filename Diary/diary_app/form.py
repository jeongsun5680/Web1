from django.forms import ModelForm
from .models import Story

class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = {'id', 'story_date', 'story_keyword', 'story_title', 'story_content', 'story_image'}