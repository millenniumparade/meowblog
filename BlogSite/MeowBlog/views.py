from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.models import User, Sentense

def createUser(request):
    if request.method = "POST":
        user = User()
        user.save()


def deleteUser(request):
    ...


def updateUser(request):
    ...


def readUser(request):
    ...

def generateContent(request):
    ...


def viewContent(request, num):
    ...