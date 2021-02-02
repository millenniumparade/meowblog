from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import User, Sentense
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse(request)
    
@csrf_exempt
def createUser(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        newUser = User(username=data["username"], password=data["password"])
        newUser.save()
    return HttpResponse(status=201)


def deleteUser(request):
    if request.method == 'DELETE':
        data = json.loads(request.body.decode('utf-8'))
        user = User.object.get(username=data["username"])
        user.delete()
        return HttpResponse(status=200) 


def updateUser(request):
    if request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        user = User.object.get(username=data["username"])
        user.password = data["newPassword"]
        user.save()
        return HttpResponse(status=200) 


def readUser(request):
    if request.method == 'GET':
        data = json.loads(request.body.decode('utf-8'))
        user = User.object.get(username=data["username"])
        return HttpResponse(user)

def generateContent(request):
    html = "<html><body>Generate content</body></html>"
    return HttpResponse(html) 


def viewContent(request, num):
    html = "<html><body>View content</body></html>"
    return HttpResponse(html) 