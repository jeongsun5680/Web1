from django.shortcuts import render
from .models import Story
from .form import StoryForm
from django.http import HttpResponseRedirect
from django.urls import reverse
#from django.forms.models import model_to_dict
#from django.http import HttpResponseRedirect
#from django.urls import reverse
#from .models import Todo

def index(request):
    stories = Story.objects.all() #objects는 클래스 변수로 되어있다
    num = Story.objects.count()
    if num==0:
        latest_story = 0
    else:
        latest_story = Story.objects.last()
    context = {"stories":stories, "latest_story":latest_story}
    #tmp_stories = Story.objects.all()
    #print(model_to_dict(tmp_stories))
    return render(request, 'index.html', context)

def writeDiary(request):
    print(request.POST)
    new_story = StoryForm(request.POST, request.FILES)
    
    new_story.save()
    return HttpResponseRedirect(reverse('index'))

def deleteDiary(request):
    story_id = request.POST.get('story_id')
    delete_story = Story.objects.get(id=story_id)
    delete_story.delete()
    return HttpResponseRedirect(reverse('index'))

def modifyDiary(request):
    story_id = request.POST.get('story_id')
    update_story = Story.objects.get(id=story_id)
    form = StoryForm(request.POST, request.FILES)
    if form.is_valid():
        #print(form.cleaned_data)
        update_story.story_date = form.cleaned_data['story_date']
        update_story.story_keyword = form.cleaned_data['story_keyword']
        update_story.story_title = form.cleaned_data['story_title']
        update_story.story_content = form.cleaned_data['story_content']
        if form.cleaned_data['story_image'] is None:
            update_story.story_image = update_story.story_image
        else:
            update_story.story_image = form.cleaned_data['story_image']
        #update_story.story_image = form.cleaned_data['story_image']
        update_story.save()
    return HttpResponseRedirect(reverse('index'))
    