from django.shortcuts import render

# Create your views here.

def carousel(request):
    return render(request,'carousel.html')