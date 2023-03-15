from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Story
import json

# Create your views here.
def Index(request):
    # Testing how to JSON in python django.
    # In this function we are return a simple JSON.
    # json.dumps() => python -> JSON
    # json.loads() JSON -> python
    x = {"name": "Hola", "age": 24}
    return HttpResponse(json.dumps(x))

def AllStories(request):
    # We need to make a list because originally Story.objects.all is a queryset, which cannot be json serializable.
    # With this we can then conver the list into a JSON. 
    AllStories = list(Story.objects.values()) 
    return JsonResponse(AllStories, safe=False)

def StoryById(request, story_id):
    IdStory = dict(Story.objects.filter(pk = story_id))
    return JsonResponse(IdStory, safe=False)