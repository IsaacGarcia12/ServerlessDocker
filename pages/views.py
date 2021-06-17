from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
HOME_PAGE_MSG = getattr(settings, "HOME_PAGE_MSG", "MISSING MESSAGE")

def Home_view(request):
    return HttpResponse(f"<h1>{HOME_PAGE_MSG}</h1>")