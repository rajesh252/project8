from django.shortcuts import render

# Create your views here.
def rajesh(request):
    return render(request,'rajesh.html',context={'name':'rajesh','age':23})