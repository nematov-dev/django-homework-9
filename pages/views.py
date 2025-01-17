from django.shortcuts import render
from django.contrib import messages

from . import forms

def home_page_views(request):
    return render(request,'index.html')

def contact_page_views(request):
    if request.method == "GET":
        return render(request,'pages/contact.html')
    elif request.method == "POST":
        form = forms.ContactPageForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message send succesfull')
        return render(request,'pages/contact.html')
        

def about_page_views(request):
    if request.method == "GET":
        return render(request,'pages/about.html')
    elif request.method == "POST":
        form = forms.ContactAboutPageForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message send succesfull')
        return render(request,'pages/about.html')

