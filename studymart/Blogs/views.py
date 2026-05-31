from django.shortcuts import render
from django.http import HttpResponse
from .forms import TeachersRegistration

# Create your views here.
def blog1(request):
    return render(request, 'blogs/blog.html')
def blog2(request):
    return render(request, 'blogs/blog2.html')
def showformsdata(request):
    if request.method == 'POST':
        fm = TeachersRegistration(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['password'])
            print(fm.cleaned_data['repassword'])
            print('This is POST statement')
    else:
        fm = TeachersRegistration()
        print('This is GET statement')
    fm.order_fields(field_order=['email', 'first_name', 'last_name'])
    return render(request, 'blogs/form.html', {'form': fm})