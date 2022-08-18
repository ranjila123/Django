from django.shortcuts import render
from . import views

from .forms import ImageForms
from .models import Image
# Create your views here.

def upload(request):
    if request.method =='POST':
         form = ImageForms(request.POST, request.FILES)
         if form.is_valid():
            form.save()
    form = ImageForms()
    img = Image.objects.all()
    return render(request, 'upload.html', {'img':img, 'form':form})


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')