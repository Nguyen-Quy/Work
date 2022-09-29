from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def post_list(request):
    return HttpResponse("You get a post list here")
