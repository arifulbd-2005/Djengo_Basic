from django.shortcuts import render
from django.http import HttpResponse
from .forms import TeachersRegistration

# Create your views here.
def blog1(request):
    return render(request, 'blogs/blog.html')
def blog2(request):
    return render(request, 'blogs/blog2.html')
def showformsdata(request):
    fm = TeachersRegistration()
    fm.order_fields(field_order=['email', 'first_name', 'last_name'])
    return render(request, 'blogs/forms.html', {'form': fm})