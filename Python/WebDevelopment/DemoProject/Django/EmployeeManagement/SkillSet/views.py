from django.shortcuts import render
from django.http import HttpResponse
from .models import Skills
# Create your views here.

def homepage(request):
    return HttpResponse(
        '<h1>Welcome to Employee Management</h1>'
    )

def updateskillset(request):
    if request.method == 'POST':
        email = request.POST['email']
        skillset = ",".join(request.POST.getlist('skills'))
        data = Skills(emailid = email, skills = skillset)
        data.save()
        return render(request,'updateskill.html',{'success':'Skill set updated successfully'})
    return render(request,'updateskill.html') 