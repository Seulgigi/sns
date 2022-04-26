from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request, 'main/mainpage.html')

def show(request):
    return render(request, 'main/show.html')

