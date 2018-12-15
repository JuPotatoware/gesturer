# -*- coding: utf-8 -*-
from django.http import HttpResponse

HttpResponse()

def index(request):
    return HttpResponse("Hello, world. How are you? Avia.")

# Create your views here.
