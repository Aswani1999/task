
from django.shortcuts import render



def demo(request):
    # return  HttpResponse("Hello World")
    return render(request,"index.html")
