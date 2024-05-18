from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse(
        '<h1>Welcome to Employee Management</h1>'
    )

def updateskillset(request):
    #return HttpResponse(
    #    '<h1>skillset</h1>'
    #)
    return render(request,'updateskill.html')