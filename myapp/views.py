from django.shortcuts import render,redirect
from .models import Feature

# Create your views here.

def index(request):
    features = Feature.objects.all()
    return render(request,'index.html', {'features': features})

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request,'counter.html' , {'amount': amount_of_words})
