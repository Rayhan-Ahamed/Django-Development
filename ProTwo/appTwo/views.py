from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<em>My second project</em>")

def help(request):
    helpdict = {'Help_insert':'Help Page'}
    return render(request,'appTwo/help.html',context=helpdict)
