from django.shortcuts import render

def has(request):
    return render(request,'index.html1')

def lap(request):
    return render(request,'index.html2')

