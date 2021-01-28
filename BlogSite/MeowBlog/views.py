from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import User, Sentense
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")
    
def createUser(request):
    return HttpResponse("Hello") 


def deleteUser(request):
    html = "<html><body>Delete user</body></html>"
    return HttpResponse(html) 


def updateUser(request):
    html = "<html><body>Update user</body></html>"
    return HttpResponse(html) 


def readUser(request):
    html = "<html><body>Read user</body></html>"
    return HttpResponse(html) 

def generateContent(request):
    html = "<html><body>Generate content</body></html>"
    return HttpResponse(html) 


def viewContent(request, num):
    html = "<html><body>View content</body></html>"
    return HttpResponse(html) 