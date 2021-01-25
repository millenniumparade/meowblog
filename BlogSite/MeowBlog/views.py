from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_POST()
def createUser(request):
    ...


def deleteUser(request):
    ...


def updateUser(request):
    ...

@require_GET()
def readUser(request):
    ...

