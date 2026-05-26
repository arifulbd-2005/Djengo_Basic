from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog1(request):
    return render(request, 'blogs/blog.html')
def blog2(request):
    return render(request, 'blogs/blog2.html')