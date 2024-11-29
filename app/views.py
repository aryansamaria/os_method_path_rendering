from django.shortcuts import render

# Create your views here.
def moon(request):
    return render(request,'moon.html')
