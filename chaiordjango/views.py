from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the chaiordjango index.")

def about(request):
    return HttpResponse("Hello, world. You're at the chaiordjango about.")

def contact(request):
    return HttpResponse("Hello, world. You're at the chaiordjango contact.")